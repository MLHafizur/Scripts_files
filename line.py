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
#im = Image.new('RGBA', (400, 400), (0, 255, 0, 0)) 
imagePaths = list(paths.list_images(folder_selected))

directory = 'output'

if not os.path.exists(directory):
    os.makedirs(directory)
print(len(imagePaths))
for (i, imagePath) in enumerate(imagePaths):
    name = imagePath.split(os.path.sep)[-1]
    coordinate_lists=[]
    print(imagePath)
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
        coordinate_lists.append(coordinate)
    plt.close()
    flat_list = [item for sublist in coordinate_lists for item in sublist]
    b = [i for sub in flat_list for i in sub]
    draw.line((flat_list[0],flat_list[1]), fill=255 ,width=5)
    draw.line((flat_list[2],flat_list[3]), fill=255 ,width=5)
    #im_pil.show()
    name_image=os.path.join(directory,name)
    im_pil.save(name_image,'JPEG')
