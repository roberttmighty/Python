#!/usr/bin/python3

#Modules
import os, shutil, datetime

#Variables
TODAY = datetime.date.today().strftime("%Y%m%d")
YEAR = datetime.datetime.now().year
l_src = "source directory"
l_dest ="destination directory/%d/" % YEAR
_ext = ".xlsx"
file_name = "name_you_want" + TODAY + _ext


#Code Start

if not os.path.exists(l_dest):
        os.makedirs(l_dest)

for filename in os.listdir(l_src):
        if filename.endswith(_ext):
                file_src = l_src + filename
                file_dest = l_src + file_name
                os.rename(file_src, file_dest)

shutil.move(l_src + file_name, l_dest + file_name)
