import glob
import os
path1=r"lbls"
path2=r"imgs"
os.chdir('data')
# label_txt_files = os.listdir(r"data")
# img_files = os.listdir(r"data")

img_files = glob.glob("*.jpg")
label_txt_files = glob.glob("*.txt")
print(len(img_files))
n = 0
count=0
list_f = []

for x in img_files:
    n=0
    x_c=x
    x=x.replace(".jpg.jpg","")
    x=x.replace(".bmp.jpg","")
    x=x.replace(".png.jpg","")
    x=x.replace(".jpeg.jpg","")
    x=x.replace(".jpg","")
    x=x.replace(".JPG","")
    x=x.replace(".jpeg","")
    x=x.replace(".png","")


    for y in label_txt_files:
        # y=y.replace(".jpg.jpg","")
        # y=y.replace(".bmp.jpg","")
        y_c=y
        y=y.replace(".jpg.txt","")
        y=y.replace(".bmp.txt","")
        y=y.replace(".png.txt","")
        y=y.replace(".jpeg.txt","")
        y=y.replace(".txt","")
        #print(y)
        if x==y:
            count=count+1
            print(x_c,y_c)
            os.rename(x_c,str(count)+".jpg")
            os.rename(y_c,str(count)+".txt")

            n=1
            break
    if n==0:
        print(x)
print(count)