import glob
# give path to your yolov4 annotation folder
txt_files = glob.glob(r"/media/Random_Images_test/*.txt")
print(len(txt_files))
# print(all_files)
n = 0
list_f = []
for x in txt_files:
    f = open(x, "r")
    for line in f.readlines():
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_f.append(line_list)
flat_list = []
for sub in list_f:
    for item in sub:
        flat_list.append(item)
print(len(list_f))
print(len(flat_list))
# make list of your classes with name
person = []
cars = []
Animals = []
Faces = []
# create more if loop if you have more classes
for c in flat_list:
    if c == '0':
        person.append(c)
    if c == '1':
        cars.append(c)
    if c == '2':
        Animals.append(c)
    if c == '3':
        Faces.append(c)


print("Person  : ", len(person))
print("Cars    : ", len(cars))
print("Animals : ", len(Animals))
print("Faces   : ", len(Faces))
