#!/usr/bin/python3

"""
Custom SPC Script to upload the daily file to B&N Portal for processing and
move .zip file to archive.

Last Update  : 08/14/2020 by Josh Westmoreland
Changes Made : Changed _RDIR variable to full remote path plus File.
Next Steps   :

"""
import pysftp, paramiko, os, shutil, datetime

#Variables
TODAY =  datetime.date.today().strftime("%Y%m%d")
YEAR = datetime.datetime.now().year
SRC_FLDR = "/psdata/b_n/bn_portal/"
FILE_NAME = TODAY + "_spcollege.bncroster.zip"
SRC_FILE = SRC_FLDR + FILE_NAME
DST_FLDR = SRC_FLDR + "archive/%d/" % YEAR 

#SFTP Connection Variables
r_HN = "rex-sftp.bncollege.com"
r_UN = "bnc8046"
r_PK = "/oracle/PSAdmin_Files/scripts/app_servers/sftp/keys/bn_bookstore_portal_private.ppk"
r_PKPW = "BNBookstorePortal0427"

#Define Functions
def s_create(folder): #Checks for destination spcifiec in argument and if not present creates it.
    if not os.path.exists(folder):
        os.makedirs(folder)

def s_move(): #Moves file from source folder to destination by name.
    shutil.move(SRC_FILE, DST_FLDR + FILE_NAME)


def s_put(HN, UN, PK, PKPW): #Connects to remote host via sftp and uploads file.
    with pysftp.Connection(host=HN, username=UN, private_key=PK, private_key_pass=PKPW) as sftp:
        sftp.cwd('/bned-sis-oneroster-mailbox-prod/data/IC8046/inbox/')
        _RDIR = '/bned-sis-oneroster-mailbox-prod/data/IC8046/inbox/' + FILE_NAME
        sftp.put(SRC_FILE, _RDIR)
            

#Start
s_put(r_HN, r_UN, r_PK, r_PKPW)
s_create(DST_FLDR)
s_move()
