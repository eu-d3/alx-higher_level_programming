#!/usr/bin/python3
import os
import shutil
"""
Makes and initializes a directory
"""
def init_dir(dir_name):
    if dir_name!='nvm':
        os.mkdir(dir_name)
        shutil.copy('misc.py', dir_name)
        os.chdir(dir_name)
        os.system('echo "To be updated, shortly" > README.md')
        os.system('git status')
        os.system('git add .')
        os.system('echo "Type a message: "')
        os.system('read message')
        os.system('echo $message')
init_dir(input("Name: "))
    

