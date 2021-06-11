import glob
import os
txt_files = os.listdir("data/modified_label/")
print(len(txt_files))
# print(all_files)
n = 0
list_f = []
for x in txt_files:
    op = os.path.join(r"data/modified_label/", x)
    f = open(op, "r")
    n_file_path = os.path.join(r"result/")
    new_file_name = os.path.join(n_file_path+x)
    new_file = open(new_file_name, "w")
    for line in f.readlines():
        stripped_line = line.strip()
        line_list = stripped_line.split()
        # list_f.append(line_list)
        print(stripped_line)
        # print(line_list)
        # print(line_list[0])
        new_file.write(
            "0"+" "+line_list[1]+" "+line_list[2]+" "+line_list[3]+" "+line_list[4])
        new_file.write("\n")
    f.close()
    new_file.close()
