__author__='Shangrui Yang'

import pandas as pd
import glob
import sys

input_path = ""

all_files = glob.glob("C:\\Users\\73419\\Desktop\\dataset\\set2\\*.csv")
i = 0
l = len(all_files)

for file in all_files:
    i += 1
    percent = int( (i / l)*100.0)
    sys.stdout.write("\r当前进度: %s%% "%(percent))
    sys.stdout.flush()  
    data_frame = pd.read_csv(file)
    data_frame.drop_duplicates(inplace=True)
    data_frame.to_csv(file, index=False)
