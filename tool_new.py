import cv2
import numpy as np
from imutils import paths
from PIL import Image, ImageDraw
from matplotlib import lines as mpl_lines
from matplotlib import pyplot as plt 
from tkinter import filedialog
from tkinter import *
import PIL.Image
import os, os.path
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
imagePaths = list(paths.list_images(folder_selected))
directory = 'output'
if not os.path.exists(directory):
    os.makedirs(directory)
print(len(imagePaths))
for (i, imagePath) in enumerate(imagePaths):
    name = imagePath.split(os.path.sep)[-1]
    coordinate_lists=[]
    img = cv2.imread(imagePath)
    height, widthx, channels = img.shape
    print(height,widthx) 
    img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = PIL.Image.fromarray(img_copy)
    draw = ImageDraw.Draw(im_pil)
    for line in range(0,2):
        plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
        plt.xticks([]), plt.yticks([])
        print("Please click 2 points to draw line :", line+1)
        coordinate = plt.ginput(2)
        print("clicked points coordinate are ", coordinate)
        b = [i for sub in coordinate for i in sub]
        if coordinate == [] or coordinate[0]==[] or len(coordinate)<2:
            print("skip image")
        elif (b[0]==b[2] and b[1]==b[3]):
            print("Skip Image")
        elif (b[0]==b[2]):
            print("Straight lline height")
            draw.line(((b[0],0), (b[0],height)), fill=128 ,width=10)
        elif(b[1]==b[3]):
            print("Straight line Width")
            draw.line(((0,b[1]), (widthx,b[1])), fill=128 ,width=10)

        elif (b[0] < b[2] and b[1] < b[3]):
            print("Top left to bottom right Error")
            slope_line1=(b[3]-b[1])/(b[2]-b[0])
           # slope_line2=(b[1]-b[3])/(b[0]-b[2])
            slope_line2=(b[2]-b[0])/(b[3]-b[1])
            intercept = b[1] - slope_line1*b[0]
            intercept2 = b[3] - slope_line2*b[2]
            print(intercept2)
            x=coordinate[0]
            y=coordinate[1]
            draw.line(((y ),(0,intercept)), fill=128 ,width=10)
            #coordinate_lists.append(coordinate)or (b[0] > b[2] and b[1] > b[3])
        elif (b[0] > b[2] and b[1] > b[3]):
            slope_line1=(b[3]-b[1])/(b[2]-b[0])
            slope_line2=(b[2]-b[0])/(b[3]-b[1])
            intercept = b[1] - slope_line1*b[0]
            intercept2 = b[2] - slope_line2*b[3]
            x=coordinate[0]
            y=coordinate[1] 
            draw.line((x,(0,intercept)), fill=128 ,width=10)  
            
        else:
            print("left bottom to right top")
            slope_line1=(b[3]-b[1])/(b[2]-b[0])
            slope_line2=(b[2]-b[0])/(b[3]-b[1])
            intercept = b[1] - slope_line1*b[0]
            intercept2 = b[2] - slope_line2*b[3]    
            # x=coordinate[0]
            # y=coordinate[1]
            draw.line(((0,intercept), (intercept2,0)), fill=128 ,width=10)
    plt.close()
    im_pil.show()
    a=1000
# flat_list = [item for sublist in coordinate_lists for item in sublist]
# b = [i for sub in flat_list for i in sub]

# im_pil.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()