#!/usr/bin/python3

#Import  modules
import pysftp, paramiko, os, shutil, datetime

#Move Variables
YEAR = datetime.datetime.now().year
_LOCDIR = "/psdata/focus2/"
l_SRC_FILES=os.listdir(_LOCDIR)
l_DEST1 ="/psdata/focus2/archive/%d/" % YEAR
l_DEST2 ="/psdata/focus2/logs/"
_csv = ".csv"
_log = ".log"

#SFTP Connection Variables
r_HN = "hostname"
r_UN = "username"
r_PW = "password"

#Define Functions
def s_create(folder): #Checks for destination specified in argument and if not present creates it.
    if not os.path.exists(folder):
        os.makedirs(folder)   
def s_move(folder, file_ext): #Moves argument specified file type to argument specified folder
    for file in l_SRC_FILES: 
        if file.endswith(file_ext):
            shutil.move(os.path.join(_LOCDIR,file), os.path.join(folder),file)
def s_get_remove(HN, UN, PW, SRC): #Connects to remote host via sftp downloads and then deletes source files
    with pysftp.Connection(host=HN, username=UN, password=PW) as sftp:
        _LOCDIR = SRC
        _RDIR = sftp.listdir(r"/")
        for files in _RDIR:
            if files.endswith(_csv):
                sftp.get(files, _LOCDIR + files)
                sftp.remove(files) 

s_create(l_DEST1)
s_move(l_DEST1, _csv)
s_move(l_DEST2, _log)
s_get_remove(r_HN, r_UN, r_PW, _LOCDIR)
