"""
These are ultility scripts used in input, output file
"""

import os
import csv
import pandas as pd


# read input
PATH = os.getcwd() + '\\input\\'


def read_file(file_name):
    """
    Read file to python list
    """
    # data = pd.read_csv(PATH + file_name + '.csv', index_col=0)
    # id_name = file_name[:-1] + '_' + 'id'
    # if data.index.name == 'id':
    #     data.index.name = id_name
    # return data
    information = []
    with open(PATH + file_name + '.csv') as file:
        reader = csv.DictReader(file)
        for _ in reader:
            information.append(_)
    return information
