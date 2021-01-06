__author__='Shangrui Yang'

'''
这个脚本用于删除csv中的重复行
'''

import pandas as pd
import glob
import sys


all_files = glob.glob(r"D:\PythonProjects\dataset\set1\*\*.csv")
i = 0
l = len(all_files)

for file in all_files:
    i += 1
    percent = int( (i / l)*100.0)
    sys.stdout.write("\r当前进度: %s%% "%(percent))
    sys.stdout.flush()  
    data_frame = pd.read_csv(file)
    data_frame.drop_duplicates(subset=['Times'], inplace=True)
    data_frame.to_csv(file, index=False)
