# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:17:42 2023

@author: 23257
"""
import os
# import shutil
import zipfile

def unzip_file(zip_file_name,destination_path,csv=False):
    archive = zipfile.ZipFile(zip_file_name,mode='r')
    if csv==True:
        for file in archive.namelist():
            if file.endswith(".csv"):
                archive.extract(file, destination_path);
    else:
        for file in archive.namelist():
            archive.extract(file, destination_path);
# lst=[];
# new_ws=[];
# lst1=[];
file_flag = '.zip'   #修改需解压的格式 例如：.rar
rootdir=r"D:\AppData\PyCode\time\WuHan\hksl2021";
new_file_zip=rf"{rootdir}\zip";
os.makedirs(new_file_zip,exist_ok=True); #创建目录存放文件
# for root, dirs, files in os.walk(rootdir):
#     for f in files:
#         lst.append(os.path.join(root, f));#遍历所有文件
#         if f.endswith(file_flag): 
#             zip_path=os.path.join(root, f);
#             # new_ws = os.path.join(new_file, f.replace(file_flag, '')) ;
#             unzip_file(zip_path,new_file);

for root, dirs, files in os.walk(rootdir,topdown=True):
    for f in files:
        # lst.append(os.path.join(root, f));#遍历所有文件
        if f.endswith(file_flag): 
                zip_path=os.path.join(root, f);
                # new_ws = os.path.join(new_file, f.replace(file_flag, '')) ;
                unzip_file(zip_path,new_file_zip);
    break;

new_file_csv=rf"{rootdir}\csv";
os.makedirs(new_file_csv,exist_ok=True); #创建目录存放文件
for root, dirs, files in os.walk(new_file_zip,topdown=True):
    for f in files:
        # lst.append(os.path.join(root, f));#遍历所有文件
        if f.endswith(file_flag): 
                zip_path=os.path.join(root, f);
                # new_ws = os.path.join(new_file, f.replace(file_flag, '')) ;
                unzip_file(zip_path,new_file_csv,True);
    break;