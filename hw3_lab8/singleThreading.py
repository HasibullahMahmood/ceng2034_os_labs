import os
import shutil
import time

start = time.time()

jpgMagic = "ffd8ffe0"
mp3Magic = "49443303"
pngMagic = "89504e47"

os.mkdir("txtFiles")
os.mkdir("jpegFiles")
os.mkdir("mp3Files")
os.mkdir("pngFiles")


def func(from_range, upto):
    for i in range(from_range, upto):
        filename = "file" + str(i)
        f = open(filename, "rb")
        content = f.read(4).hex()
        if content == jpgMagic:
            shutil.move(filename, "./jpegFiles")
        elif content == pngMagic:
            shutil.move(filename, "./pngFiles")
        elif content == mp3Magic:
            shutil.move(filename, "./mp3Files")
        else:
            shutil.move(filename, "./txtFiles")


func(1, 5)
func(10, 150)

print("done")
print("Entire job took: " + str(time.time() - start) + " seconds")
