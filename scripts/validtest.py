import pandas as pd
import random
import data_complement

move_points = 1
path = r"D:\PythonProjects\dataset\testset.csv"



origin_data = pd.read_csv(path)
l = len(origin_data)
i = 1
move_list = random.sample(range(1, l-1), move_points)
basetime = 0

for n in move_list:
    origin_data.loc[n, 'ismoved'] = 1

while i < l-1:
    if origin_data.iloc[i]['ismoved'] == 1:
        
        j = i
        while origin_data.iloc[j]['ismoved'] == 1:
            j += 1
        
        oldvalue = origin_data.iloc[i]['value']
        newvalue = (origin_data.iloc[i-1]['value'] + origin_data.iloc[j]['value']) / 2
        origin_data.loc[i, "newvalue"] = newvalue
        origin_data.loc[i, "difference"] =abs(newvalue - oldvalue) / oldvalue
    print("\r"+str(i))
    i = i + 1

print(origin_data)

print("最不精确的为：" + str(1 - max(origin_data['difference'])))

origin_data.to_csv(r"D:\PythonProjects\dataset\testset123.csv", index = False)

     


