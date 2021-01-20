#!/usr/bin/python3

#Import  modules
import pysftp, paramiko, os, datetime

#Variables
FILE_F = "/psdata/ccla/personnel/perspc_20200817.dat"
OUTPUT_F = "/psdata/ccla/logs/ccla_upload_"
TODAY = datetime.date.today().strftime("%Y%m%d")

#SFTP Connection Variables
r_HN = "hostname"
r_UN = "username"
r_PW = "password"

#Define Functions
def s_put(HN, UN, PW): #Connects to remote host via sftp and uploads files.
    with pysftp.Connection(host=HN, username=UN, password=PW) as sftp:
        _RDIR = sftp.listdir(r"/")
        sftp.put(FILE_F, _RDIR)

def s_list(HN, UN, PW): #Connects to remote hose via sftp and prints directory contents to file.
    with pysftp.Connection(host=HN, username=UN, password=PW) as sftp:
        _RDIR_LIST = sftp.listdir_attr()
        for attr in _RDIR_LIST:
            print(attr.filename, attr, file=open(OUTPUT_F + TODAY + ".log" , "a+"))

#Code Start
s_put(r_HN, r_UN, r_PW)
s_list(r_HN, r_UN, r_PW)
