#!/usr/bin/python3

"""
Custom SPC Script to upload CCLA files.

Last Update  : 06/23/2020 by Josh Westmoreland
Changes Made : Remote directory list to date stamped file on /psdata/
Next Steps   : Add email notification on completion if requested.

"""

#Import  modules
import pysftp, paramiko, os, datetime

#Variables
PERSONNEL_F = "/psdata/ccla/personnel/perspc_20200817.dat"
STUDENT_F = "/psdata/ccla/student/stuspc_05182020.dat"
OUTPUT_F = "/psdata/ccla/logs/ccla_upload_"
TODAY = datetime.date.today().strftime("%Y%m%d")

#SFTP Connection Variables
r_HN = "securefiles.flvc.org"
r_UN = "spftp"
r_PW = "0PsU$er#3"

#Define Functions
def s_put(HN, UN, PW): #Connects to remote host via sftp and uploads files.
    with pysftp.Connection(host=HN, username=UN, password=PW) as sftp:
        _RDIR = sftp.listdir(r"/")
        sftp.put(PERSONNEL_F, _RDIR)
        sftp.put(STUDENT_F, _RDIR)

def s_list(HN, UN, PW): #Connects to remote hose via sftp and prints directory contents to file.
    with pysftp.Connection(host=HN, username=UN, password=PW) as sftp:
        _RDIR_LIST = sftp.listdir_attr()
        for attr in _RDIR_LIST:
            print(attr.filename, attr, file=open(OUTPUT_F + TODAY + ".log" , "a+"))

#Code Start
s_put(r_HN, r_UN, r_PW)
s_list(r_HN, r_UN, r_PW)