#!/usr/bin/python3

"""
Custom SPC Script to delete files from Nelnet SFTP

Last Update: 06/16/2020 by Josh Westmoreland
Changes Made: Created Script
Next Steps:

"""
#Import Modules
import pysftp, paramiko, os, shutil, datetime

#Variables 
_xml = ".xml"

#SFTP Connection Varibles
r_HN = "transfer.nbspayments.com"
r_UN = "stpete_ent"
r_PK = "/oracle/PSAdmin_Files/scripts/app_servers/sftp/keys/nelnet_payments.ppk"

def s_remove(HN, UN, PK): #Connects to remote host via sftp and deletes files.
    with pysftp.Connection(host=HN, username=UN, private_key=PK) as sftp:
        sftp.cwd("/stpete/prod/")
        _RDIR = sftp.listdir()
        for files in _RDIR:
            if files.endswith(_xml):
                sftp.remove(files)

s_remove(r_HN, r_UN, r_PK)