import glob
import os
import cv2
import numpy as np
# give path of your images folder
img_files = os.listdir(
    r"C:\Users\TDF03-PC1\Desktop\concatinate_images\validation_dataset")
n = 0
le = len(img_files)
list_f = []
for i in range(0, le, 4):
    path1 = os.path.join("validation_dataset", img_files[i])
    path2 = os.path.join("validation_dataset", img_files[i+1])

    path3 = os.path.join("validation_dataset", img_files[i+2])
    path4 = os.path.join("validation_dataset", img_files[i+3])

    img1 = cv2.imread(path1)
    resize1 = cv2.resize(img1, (304, 304))
    img2 = cv2.imread(path2)
    resize2 = cv2.resize(img2, (304, 304))
    img3 = cv2.imread(path3)
    resize3 = cv2.resize(img3, (304, 304))
    img4 = cv2.imread(path4)
    resize4 = cv2.resize(img4, (304, 304))
    vis = np.concatenate((resize1, resize2), axis=1)
    vis1 = np.concatenate((resize3, resize4), axis=1)
    vis2 = np.concatenate((vis, vis1), axis=0)
    # validation_4_img/ change it according to your new folder path
    fname = "validation_4_img/"+str(i)+".jpg"
    cv2.imwrite(fname, vis2)
