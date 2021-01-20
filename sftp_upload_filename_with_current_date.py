#!/usr/bin/python3

import pysftp, paramiko, os, shutil, datetime

#Variables
TODAY =  datetime.date.today().strftime("%Y%m%d")
YEAR = datetime.datetime.now().year
SRC_FLDR = "source_directory"
FILE_NAME = TODAY + "file_name"
SRC_FILE = SRC_FLDR + FILE_NAME
DST_FLDR = SRC_FLDR + "archive/%d/" % YEAR 

#SFTP Connection Variables
r_HN = "hostname"
r_UN = "username"
r_PK = "private_key"
r_PKPW = "private_key_password"

#Define Functions
def s_create(folder): #Checks for destination spcifiec in argument and if not present creates it.
    if not os.path.exists(folder):
        os.makedirs(folder)

def s_move(): #Moves file from source folder to destination by name.
    shutil.move(SRC_FILE, DST_FLDR + FILE_NAME)


def s_put(HN, UN, PK, PKPW): #Connects to remote host via sftp and uploads file.
    with pysftp.Connection(host=HN, username=UN, private_key=PK, private_key_pass=PKPW) as sftp:
        sftp.cwd('remote_directory')
        _RDIR = 'remote_directory' + FILE_NAME
        sftp.put(SRC_FILE, _RDIR)
            

#Start
s_put(r_HN, r_UN, r_PK, r_PKPW)
s_create(DST_FLDR)
s_move()
