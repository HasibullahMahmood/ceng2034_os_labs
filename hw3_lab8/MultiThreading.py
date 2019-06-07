import os
import shutil
import threading
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


t1 = threading.Thread(target=func, args=(1, 5))
t2 = threading.Thread(target=func, args=(10, 50))
t3 = threading.Thread(target=func, args=(50, 100))
t4 = threading.Thread(target=func, args=(100, 150))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("done")
print("Entire job took: " + str(time.time() - start) + " seconds")
