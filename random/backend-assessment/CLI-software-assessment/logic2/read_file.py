import os
import csv
# read input
path = os.getcwd() + '\\input\\'


def read_file(file_name):
    with open(path + file_name + '.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        return csv_reader


courses = read_file('courses')
for row in courses:
    print(row)
