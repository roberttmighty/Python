#!/usr/bin/python3

#Import Modules
import pysftp, paramiko, os, shutil, datetime

#Variables 
_ext = "ext_you_want"

#SFTP Connection Varibles
r_HN = "hostname"
r_UN = "username"
r_PK = "private_key_file"

def s_remove(HN, UN, PK): #Connects to remote host via sftp and deletes files.
    with pysftp.Connection(host=HN, username=UN, private_key=PK) as sftp:
        sftp.cwd("remote_directory")
        _RDIR = sftp.listdir()
        for files in _RDIR:
            if files.endswith(_ext):
                sftp.remove(files)

s_remove(r_HN, r_UN, r_PK)
