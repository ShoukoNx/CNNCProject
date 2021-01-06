import os
import glob

path1 = r"D:\PythonProjects\dataset\set1"
path2 = r"D:\PythonProjects\dataset\set2"


count = [0 ,0, 0]
total = [0]


def get_size(path):
    files = os.listdir(path)
    for file in files:
        temp_path = os.path.join(path, file)
        if os.path.isdir(temp_path):
            get_size(temp_path) 
        else:
            sz = os.path.getsize(temp_path)
            total[0] += 1
            if sz > 6000 * 1024:
                count[0] += 1
            if sz > 1024 * 1024:
                count[1] += 1
            if sz > 2 * 1024 * 1024:
                count[2] += 1

        
path = r"D:\PythonProjects\dataset"
get_size(path1)

print("总共文件数："+str(total[0]))
print("大于3800kb的文件："+str(count[0]))

                
