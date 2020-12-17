__author__='Shangrui Yang'


import pandas as pd
import glob
import sys


all_files = glob.glob("C:\\Users\\73419\\Desktop\\dataset\\set1\\*.csv")
lastfile=""
writer = pd.ExcelWriter("1.xlsx")
l = len(all_files)
i = 0

for file in all_files:
    i += 1
    percent = int( (i / l)*100.0)
    sys.stdout.write("\r当前进度: %s%% "%(percent))
    sys.stdout.flush() 
    newfile = file.replace("C:\\Users\\73419\\Desktop\\dataset\\set1\\", "")
    newfile = newfile.replace(".csv", "")
    if newfile[1:4] == lastfile[1:4]:
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name=newfile, index=False)
        lastfile = newfile
    else:
        writer.save()
        lastfile = newfile
        writer = pd.ExcelWriter("C:\\Users\\73419\\Desktop\\dataset\\set1merge\\"+newfile[1:4]+".xlsx")
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name=newfile, index=False)
        

