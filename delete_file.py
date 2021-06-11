import glob
import cv2
txt_files = glob.glob(r"test.txt")
img_file = glob.glob(r"data\data_renew\*.jpg")
print(len(img_file))

#print(all_files)
# n = 0
list_f = []
for x in txt_files:
    f=open(x,"r")
    for line in f.readlines():
        list_f.append(line)
print(len(list_f))
count = 0
for x in img_file:
    x=str(x)
    for y in list_f:
        y=str(y)
        if x!=y:
            count=count+1
            break
print(count)
#         img=cv2.imread(r"data\obj\0de8f49f06.jpg")
#         cv2.imshow("frame",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()