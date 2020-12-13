
__author__='Shangrui Yang'

import pandas as pd
import sys

def divide(inputfile):

    origin_data_frame = pd.read_csv(inputfile)

    l = len(origin_data_frame)
    firstrow = origin_data_frame.iloc[0]
    i = 0
    lastPoint = firstrow['pointname']
    curPoint = firstrow['pointname']
    preptr = 0

    while i < l:
        percent = int( (i / l)*100.0)
        sys.stdout.write("\r当前进度: %s%% "%(percent))
        sys.stdout.flush()  
        row = origin_data_frame.iloc[i]
        curPoint = row['pointname']
        if curPoint == lastPoint:
            i = i + 1
        else:
            processed_data_frame = origin_data_frame.iloc[preptr:i][['times', 'numvalue']]
            processed_data_frame.columns = ['Times',lastPoint]
            outputfile = "D:\\dataset2\\"+lastPoint+'.csv'
            processed_data_frame.to_csv(outputfile, index=False)
            lastPoint = curPoint
            preptr = i


if __name__ == "__main__":
    divide("C:\\Users\\Shouko\\Desktop\\python\\dataset\\his_point2.csv")
    