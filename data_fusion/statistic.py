import pandas as pd

#文件导入
origin_data_frame = pd.read_csv("test.csv")
processed_data_frame = pd.DataFrame(columns=["JobName", "SizeX", "SizeY", 
"Mean_PerArea", "Mean_PerVolume"])


#初始参数设定
standard_X = origin_data_frame.loc[0,'SizeX(um)']
standard_Y = origin_data_frame.loc[0,'SizeY']
max_PerArea = 0
min_PerArea = 10000000
max_PerVolume = 0
min_PerVolume = 10000000
perArea_set = pd.Series()
perVolume_set = pd.Series()



for index, row in origin_data_frame.iterrows():
    if row['SizeX(um)'] == standard_X and row['SizeY'] == standard_Y:
        cur_area = row['PerArea(%)']
        cur_volume = row['PerVolume(um)']
        perArea_set = perArea_set.append(pd.Series([cur_area]))
        perVolume_set = perVolume_set.append(pd.Series([cur_volume]))

    else:
        count = perVolume_set.count();

        mean_area = perArea_set.mean()
        max_PerArea = perArea_set.max()
        min_PerArea = perArea_set.min()
        var_PerArea = perArea_set.var() if count > 1 else 0

        mean_volume = perVolume_set.mean()
        max_PerVolume = perVolume_set.max()
        min_PerVolume = perVolume_set.min()
        var_PerVolume = perVolume_set.var() if count > 1 else 0


        processed_data_frame = processed_data_frame.append([{'JobName':row["JobName"], 'SizeX':standard_X, 'SizeY':standard_Y, 
        'Mean_PerArea':mean_area, 'Max_PerArea':max_PerArea,'Min_PerArea':min_PerArea,
        'Var_PerArea':var_PerArea,
        'Mean_PerVolume':mean_volume, 'Max_PerVolume':max_PerVolume,
        'Min_PerVolume':min_PerVolume, 'Var_PerVolume':var_PerVolume,
        'Count':count}], 
        ignore_index=True, sort = False)

        standard_X = row['SizeX(um)']
        standard_Y = row['SizeY']

        perArea_set = pd.Series(row['PerArea(%)'])
        perVolume_set = pd.Series(row['PerVolume(um)'])


#保存处理后的文件
processed_data_frame.to_csv("processed.csv")






