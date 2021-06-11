import cv2
import os
import glob
img_files = os.listdir(r"car_data")
save_path = os.path.join(r"car_resize/")
for x in img_files:
    path=os.path.join(r"car_data/",x)
    img = cv2.imread(path)
    #cv2.imshow("ss",img)
    resize = cv2.resize(img,(608,608))
    fname = save_path + x
    cv2.imwrite(fname,resize)