__author__='Shangrui Yang'


import pandas as pd
import glob
import sys
import os


all_files = glob.glob("C:\\Users\\73419\\Desktop\\dataset\\set2\\*.csv")

for file in all_files:
    newfile = file.replace("_AVALUE", "")
    os.rename(file, newfile)

'''
writer = pd.ExcelWriter(".xlsx")
for file in files:
    df = pd.read_csv(file)
    df.to_excel(writer,sheet_name=file)
    
writer.save()
'''