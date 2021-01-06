import os, shutil
import glob
import pandas as pd

all_files = glob.glob(r"D:\PythonProjects\dataset\set2\*\*.csv")

for file in all_files:
    df = pd.read_csv(file)
    l = len(df)
    if (l-1) / 518400 > 0.5 :
        fpath,fname=os.path.split(file)
        dsfile = os.path.join(r"D:\PythonProjects\dataset\select2\\", fname)
        shutil.copyfile(file, dsfile)
        