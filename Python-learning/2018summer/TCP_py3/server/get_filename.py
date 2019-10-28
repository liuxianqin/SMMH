#coding=utf-8

import os

def get_filename(file_dir):
    for root,dirs,files in os.walk(file_dir):
#print(root)
#print(dirs)
        print(files)

get_filename('.')


