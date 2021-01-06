import os
import glob

path1 = r"D:\PythonProjects\dataset\set1"
path2 = r"D:\PythonProjects\dataset\set2"

SZ = 500 * 1024

def remove(path):
    files = os.listdir(path)
    for file in files:
        temp_path = os.path.join(path, file)
        if os.path.isdir(temp_path):
            remove(temp_path)
            if not os.listdir(temp_path):
                os.rmdir(temp_path)          
        else:
            sz = os.path.getsize(temp_path)
            if sz < SZ:
                os.remove(temp_path)


        
remove(path1)
