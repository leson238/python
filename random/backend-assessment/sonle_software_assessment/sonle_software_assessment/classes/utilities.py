"""Import"""
import os
import csv

# Prettify my exception
import sys
sys.tracebacklimit = 0

# read input
PATH = os.getcwd()


def read_file(file_name):
    """Read file to python list"""
    information = []
    with open(f"{PATH}\\input\\{file_name}.csv") as file:
        reader = csv.DictReader(file)
        for _ in reader:
            information.append(_)
    return information


def write_file(file_name='reports', subfolder='', extension='txt', data=''):
    """ Write file to custom directory, default parent directory"""
    subfolder = f"{subfolder}\\" if (subfolder != '') else ''
    with open(f"{PATH}\\{subfolder}{file_name}.{extension}", "w+") as file:
        file.write(data)
