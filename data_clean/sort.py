
__author__='Shangrui Yang'

import pandas as pd
import sys

def sortdata(inputfile):

    origin_data_frame = pd.read_csv(inputfile)

    origin_data_frame.sort_values(by=['pointname', 'times'], inplace=True)

    origin_data_frame.to_csv("G:\\crrc\\new1.csv", index=False)


if __name__ == "__main__":
    sortdata("G:\\crrc\\original\\his_point1.csv")
    