__author__='Shangrui Yang'


import pandas as pd
import glob
import sys
import os
import shutil


all_files = glob.glob("C:\\Users\\73419\\Desktop\\dataset\\set2\\*.csv")
l = len(all_files)
i = 0

for file in all_files:
    i += 1
    percent = int( (i / l)*100.0)
    sys.stdout.write("\r当前进度: %s%% "%(percent))
    sys.stdout.flush() 
    newfile = file.replace("C:\\Users\\73419\\Desktop\\dataset\\set2\\", "")
    newfile = newfile.replace(".csv", "")
    newpath = "C:\\Users\\73419\\Desktop\\dataset\\set2merge\\"+newfile[1:4]
    isExists = os.path.exists(newpath)
    if not isExists:
        os.makedirs(newpath)
    shutil.copy(file, newpath+"\\"+newfile+".csv")