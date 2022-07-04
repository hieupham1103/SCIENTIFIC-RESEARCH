from PIL import Image
from os import walk
import glob
import os

# name = "Seiken Gakuin no Maken Tsukai"

filelist = []
for (dirpath, dirnames, filenames) in walk("./Input"):
    filelist.extend(filenames)

for i in filelist:
    # i = i[7:]
    print(f"./Input/Chap {i[7:]}")
    os.rename(f"./Input/{i}", f"./Input/Chap{i[7:]}")