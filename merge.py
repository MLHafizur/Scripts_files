import glob
import os
face_txt_files = os.listdir("data/face_label_acc")
person_txt_files = os.listdir("data/person_labels")

# n=0
# for x in face_txt_files:
#     if ".bmp.jpg.txt" in x:
#         y=x.replace(r".bmp.jpg.txt",r".bmp.txt")
#         op=os.path.join(r"data/face_label",x)
#         op1=os.path.join(r"data/face_label",y)

#         print(op)
#         os.rename(op,op1)
# print(n)

n = 0
list_f = []
for x in person_txt_files:
    for y in face_txt_files:
        #print(y)
        if x==y:
            op=os.path.join(r"data/person_labels",x)
            op1=os.path.join(r"data/face_label_acc",y)
            
            file_person=open(op,"r")
            data0=file_person.read()

            file_face=open(op1,"r")
            data1=file_face.read()
            print(data1)
            print(data0)
            file_person.close()
            file_face.close()
            break
    n_file_path=os.path.join(r"result/")
    new_file_name=os.path.join(n_file_path+x)
    new_file=open(new_file_name,"w")
    data0 += data1 
    new_file.write(data0)
#print(n)

#     f=open(x,"r")
#     for line in f.readlines():
#         stripped_line = line.strip()
#         line_list = stripped_line.split()
#         list_f.append(line_list)
#     #print(list_f)
#     #n=f.read()
#     #print(n)
# flat_list=[]
# for sub in list_f:
#     for item in sub:
#         flat_list.append(item)
# print(len(list_f))
# print(len(flat_list))
# xo = []
# for c in flat_list:
#     if c == '0':
#         xo.append(c)
# print(xo)
# print(len(xo))