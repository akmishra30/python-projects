#!/usr/bin/python

# This program is to show basic of python programming
# I'm opening a file using python
#

import os
import sys
import time
from datetime import datetime

# This function is to open a file
def open_file(fileName):
    print('Hello First Python program', fileName)
    
    _currDir = os.getcwd() + os.sep + 'resource' + os.sep + fileName;

    print('---> ', _currDir)

    with open(_currDir, 'r') as _fileObject:
        _fileText = _fileObject.read()

    print('---->' + _fileText)

# This function is to traverse the dir
def traverse_dir(tar_dir):
    for root, dirs, files in os.walk(tar_dir):
        print('-----------------------------')
        print('Root --', root)
        print('dirs -- ', dirs)
        t_relpath = os.path.relpath(root, tar_dir)
        print('t_relpath -- ', t_relpath)
        if t_relpath != '.': #skipped base folder processing
            for file in files:
                print('File Name: -- ', t_relpath + os.sep + file)
        print('-----------------------------')
#open_file('readme.md')

traverse_dir('/Users/makhir/Downloads/watch/')