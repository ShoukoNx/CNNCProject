

__author__='Shangrui Yang'

import pandas as pd
import glob, os, sys



def timeclean(inputfile, outputfile):
    
    origin_data_frame = pd.read_csv(inputfile)
    c2 = origin_data_frame.columns[1]
    processed_data_frame = pd.DataFrame(columns=["Times",c2])
    l = len(origin_data_frame)
    index = 1
    firstrow = origin_data_frame.iloc[0]
    processedTop = pd.Series([firstrow['Times'], firstrow[c2]], index=['Times', c2])
    processed_data_frame = processed_data_frame.append(processedTop, ignore_index=True, sort = False)
    

    while index < l:
        percent = int( (index / l)*100.0)
        sys.stdout.write("\r当前进度: %s%% "%(percent))

        baseTime = processedTop['Times']
        baseSecondstr = baseTime[-2:]
        baseSecond = int(baseSecondstr)
        row = origin_data_frame.iloc[index]
        curTime = row['Times']
        curSecondstr = curTime[-2:]
        curSecond = int(curSecondstr)

        if curSecond < baseSecond:
            curSecond += 60

        if baseSecond == curSecond:
            index = index + 1
            continue
        elif curSecond - baseSecond == 1:
            processedTop = pd.Series([row['Times'], row[c2]], index=['Times', c2])       
            processed_data_frame = processed_data_frame.append(processedTop, ignore_index=True, sort = False)
            index += 1
            continue
        else:
            value = (processedTop[c2] + row[c2]) / 2
            baseSecond += 1
            if baseSecond < 60:
                baseSecondstr = str(baseSecond)
                if baseSecond < 10:
                    baseSecondstr = "0" + baseSecondstr
                time = baseTime[0:-2] + baseSecondstr
            else:
                baseSecond = baseSecond - 60
                baseSecondstr = str(baseSecond)
                if baseSecond < 10:
                    baseSecondstr = "0" + baseSecondstr
                time = curTime[0:-2] + baseSecondstr

            processedTop = pd.Series([time, value], index=['Times', c2])
          
            processed_data_frame = processed_data_frame.append(processedTop, ignore_index=True, sort = False)

    processed_data_frame.to_csv(outputfile, index=False)

if __name__ == "__main__":


    inputfile = r"D:\PythonProjects\dataset\select1\\4VVP005MD.csv"
    outputfile = r"D:\PythonProjects\dataset\selectpro1\\4VVP005MD.csv"

    timeclean(inputfile, outputfile)
    
    '''
    all_files = glob.glob(inputfile)
    i = 0
    l = len(all_files)
    for file in all_files:
        i += 1
        percent = int( (i / l)*100.0)
        sys.stdout.write("\r当前进度: %s%% "%(percent))
        sys.stdout.flush() 
        fpath,fname=os.path.split(file)
        dsfile = os.path.join(outputfile, fname)
        timeclean(file, dsfile)
    '''




