import os

os.chdir('raw_images')
print(os.getcwd())
COUNT = 0


def increment():
    global COUNT
    COUNT = COUNT + 1


for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_name = "raw_img_" + str(COUNT)
    increment()

    new_name = '{}{}'.format(f_name, ".jpg")
    os.rename(f, new_name)
