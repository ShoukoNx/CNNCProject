import pandas as pd
import glob, os

path = r"D:\PythonProjects\dataset\selectpro1\*.csv"

all_files = glob.glob(path)

for file in all_files:
    df = pd.read_csv(file)
    l = len(df)
    print(file)
    print(l)
