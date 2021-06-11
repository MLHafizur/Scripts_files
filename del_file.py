import glob
import cv2
txt_files = glob.glob(r"train.txt")
img_file = glob.glob(r"data\data\*.jpg")
img_file_txt = glob.glob(r"data\data\*.txt")

import os
#print(all_files)
# n = 0
import shutil


count=0

target = r'C:\Users\TDF03-PC1\Desktop\fff\validation_last'
list_f = []
for x in txt_files:
    f=open(x,"r")
    for line in f.readlines():
        list_f.append(line)
# print(list_f)
for u in img_file:
    for y in list_f:
        u=u.replace("\\",'/')
        y=y.replace("\n","")
        if u==y:
            target=r"C:\Users\TDF03-PC1\Desktop\fff\train_data\train_"+str(count)+".jpg"
            target2=r"C:\Users\TDF03-PC1\Desktop\fff\train_data\train_"+str(count)+".txt"
            original=u
            original2=original.replace(".jpg",".txt")
            count=count+1
            shutil.copyfile(original, target)
            try:
                shutil.copyfile(original2, target2)  
            except:    
                print(u)
            break
print(count)