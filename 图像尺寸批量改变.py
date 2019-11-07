# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:30:01 2019

@author: lrl
"""
import cv2
import os
import numpy as np

input_path=input("请输入图片文件夹路径")
if not os.path.exists(input_path):   ##检查路径是否存在
    print("输入文件夹不存在")  
output_path=input("请输入输出文件夹路径")   
set_ratio=input("请输入目标分辨率,一般请输入0.5：")
if not os.path.exists(output_path):
    os.makedirs(output_path)   # #如果不存在则创建路径
i=0
for root ,dir ,files in os.walk(input_path):
    for file_name in files:
        if root.endswith('18') or root.endswith('16') or root.endswith('17'):
            file_root=root.split('_')
            file_root=file_root[-1].split("\\")
            print(file_root,file_name)
            ratio=float(file_root[0])
#####file_root[ration,scale]  such as  ['0.449', '18']
            ##file_name :    xxxxxxx_205165165_0.151.tif or tfw
            
            
            if file_name.endswith(".tif") : 
                ##读取所有以tif结尾的文件
                print(i+1)
                i=i+1
                #name_split=file_name.split('-')
                ratio=float(file_root[0])
                file=os.path.join(root,file_name)
                print(ratio,file,file_name)
                
                try:
                    ##imread无法读取中文文件名的图片  改用下列代码
                    img=cv2.imdecode(np.fromfile(file,dtype=np.uint8),-1)
            
                except:
                    print("文件读不了啦！")
                try:   ##改变图片尺寸大小
                    img_height,img_width=img.shape[0:2]
                    new_ratio=float(ratio/float(set_ratio))
                    size=(int(img_width*new_ratio),int(img_height*new_ratio))
                    resized=cv2.resize(img,size)
                   # resized=resize(img,ratio)
                except:
                    print("尺寸没有改变成功呀！")
                
                
                file_name=root.split('\\')
#                file_name=file_name[0].split('\\')
                file_name=set_ratio+'-'+file_name[-2]+'.jpg'    
                saved_name=str.replace(file_name,'tif','jpg')
                #saved_name=str.replace(saved_name,name_split[0],set_ratio)   ##把文件名前面的分辨率改成0.5
                saved_path=os.path.join(output_path,saved_name)
                print(saved_path)
                
                try:
                    #cv2.imwrite(saved_path,resized)  ##保存图片为了防止中文文件名乱码  用下列的代码来保存
                    cv2.imencode('.jpg', resized)[1].tofile(saved_path)
                except:
                    print("保存失败啦！")

print("图片尺寸转换完毕")