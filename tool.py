import cv2
import numpy as np
from PIL import Image, ImageDraw
from matplotlib import lines as mpl_lines
from matplotlib import pyplot as plt 
#im = Image.new('RGBA', (400, 400), (0, 255, 0, 0)) 
coordinate_lists=[]
img = cv2.imread("1398312.jpg")
height, widthx, channels = img.shape
print(height,widthx) 
img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
im_pil = Image.fromarray(img_copy)
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

if (b[0]==b[2]):
    print("Straight lline")
    draw.line(((height,b[1]), (height,b[3])), fill=128 ,width=10)
    draw.line(((height,b[5]), (height,b[7])), fill=128 ,width=10)
    #draw.line(((0,intercept_2), (intercept2_2,0)), fill=128 ,width=10)
elif(b[1]==b[3]):
    print("www")
    draw.line(((b[0],widthx), (b[2],widthx)), fill=128 ,width=10)
    draw.line(((b[4],widthx), (b[6],widthx)), fill=128 ,width=10)

elif (b[0] < b[2] and b[1]<b[3] )or (b[0]>b[2] and b[1]>b[3]):
    print("Exception")
    y=flat_list[1]
    slope_line1=(b[3]-b[1])/(b[2]-b[0])
    slope_line2=(b[2]-b[0])/(b[3]-b[1])
    intercept = b[1] - slope_line1*b[0]
    intercept2 = b[2] - slope_line2*b[3]

    slope_line1_2=(b[7]-b[5])/(b[6]-b[4])
    slope_line2_2=(b[6]-b[4])/(b[7]-b[5])
    intercept_2 = b[5] - slope_line1_2*b[4]
    intercept2_2 = b[6] - slope_line2_2*b[7]
    x=flat_list[0]
    y=flat_list[1]
    a=flat_list[2]
    b=flat_list[3]
    print(y)
    draw.line(((0,intercept), y), fill=128 ,width=10)
    draw.line(((0,intercept_2), b), fill=128 ,width=10)

else:
    slope_line1=(b[3]-b[1])/(b[2]-b[0])
    slope_line2=(b[2]-b[0])/(b[3]-b[1])
    intercept = b[1] - slope_line1*b[0]
    intercept2 = b[2] - slope_line2*b[3]
    
    slope_line1_2=(b[7]-b[5])/(b[6]-b[4])
    slope_line2_2=(b[6]-b[4])/(b[7]-b[5])
    intercept_2 = b[5] - slope_line1_2*b[4]
    intercept2_2 = b[6] - slope_line2_2*b[7]
    x=flat_list[0]
    y=flat_list[1]
    a=flat_list[2]
    b=flat_list[3]
    draw.line(((0,intercept), (intercept2,0)), fill=128 ,width=10)
    draw.line(((0,intercept_2), (intercept2_2,0)), fill=128 ,width=10)

im_pil.show()
cv2.waitKey(0)
cv2.destroyAllWindows()