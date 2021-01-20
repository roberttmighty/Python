#!/usr/bin/python3

"""
Custom SPC Script to rename and move xls from Work From Home PS Query.

Last Update  : 08/24/2020 by Josh Westmoreland
Changes Made : Removed Functions, Updated Move to use file name instead of
               file extension.
Next Steps   : Test

"""
#Modules
import os, shutil, datetime

#Variables
TODAY = datetime.date.today().strftime("%Y%m%d")
YEAR = datetime.datetime.now().year
l_src = "/psdata/work_from_home/"
l_dest ="/psdata/work_from_home/%d/" % YEAR
_ext = ".xlsx"
file_name = "work_from_home_" + TODAY + _ext


#Code Start

if not os.path.exists(l_dest):
        os.makedirs(l_dest)

for filename in os.listdir(l_src):
        if filename.endswith(_ext):
                file_src = l_src + filename
                file_dest = l_src + file_name
                os.rename(file_src, file_dest)

shutil.move(l_src + file_name, l_dest + file_name)