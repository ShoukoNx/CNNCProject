

__author__='Shangrui Yang'

import pandas as pd



def timeclean(inputfile, outputfile):
    
    origin_data_frame = pd.read_csv(inputfile)
    processed_data_frame = pd.DataFrame(columns=["times","4RPN410KM"])

    l = len(origin_data_frame)
    index = 1
    firstrow = origin_data_frame.iloc[0]
    processedTop = pd.Series([firstrow['times'], firstrow['numvalue']], index=['times', '4RPN410KM'])
    processed_data_frame = processed_data_frame.append(processedTop, ignore_index=True, sort = False)
    

    while index < l:
        baseTime = processedTop['times']
        baseSecondstr = baseTime[-2:]
        baseSecond = int(baseSecondstr)
        row = origin_data_frame.iloc[index]
        curTime = row['times']
        curSecondstr = curTime[-2:]
        curSecond = int(curSecondstr)

        if curSecond < baseSecond:
            curSecond += 60

        if baseSecond == curSecond:
            index = index + 1
            continue
        elif curSecond - baseSecond == 1:
            processedTop = pd.Series([row['times'], row['numvalue']], index=['times', '4RPN410KM'])       
            processed_data_frame = processed_data_frame.append(processedTop, ignore_index=True, sort = False)
            index += 1
            continue
        else:
            value = (processedTop['4RPN410KM'] + row['numvalue']) / 2
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

            processedTop = pd.Series([time, value], index=['times', '4RPN410KM'])
          
            processed_data_frame = processed_data_frame.append(processedTop, ignore_index=True, sort = False)

    processed_data_frame.to_csv(outputfile, index=False)

if __name__ == "__main__":
    inputfile = "C:\\Users\\73419\\Desktop\\dataset\\his_point.csv" 
    outputfile = "C:\\Users\\73419\\Desktop\\dataset\\4RPN410KM.csv"
    timeclean(inputfile, outputfile)




