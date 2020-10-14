"""Import"""
import time
import os
from classes.Student import Student, STUDENTS_TABLE
from classes.utilities import write_file, PATH

START = time.time()

STUDENTS = []
for record in STUDENTS_TABLE:
    STUDENTS.append(Student(record['id'], record['name']))

DATA = ''.join(list(map(str, STUDENTS)))
write_file(data=DATA)

END = time.time()

with open('reports.txt') as file:
    LENGTH = len(file.readlines())
    print(f"Done writing {LENGTH} lines in {(END - START):.3f} seconds")

os.system(f'start "" {PATH}\\reports.txt')
