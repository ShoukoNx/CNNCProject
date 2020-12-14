__author__='Shangrui Yang'


import pandas as pd
import glob
import sys


all_files = glob.glob("C:\\Users\\73419\\Desktop\\dataset\\set2\\*.csv")
l = len(all_files)
i = 0

for file in all_files:
    i += 1
    percent = int( (i / l)*100.0)
    sys.stdout.write("\r当前进度: %s%% "%(percent))
    sys.stdout.flush() 
    df = pd.read_csv(file)
    newcol = df.columns[1].replace("_AVALUE", "")
    df.columns=['Times', newcol]
    df.to_csv(file, index=False)


