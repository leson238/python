"""
A program that exports students' report to reports.txt file. 
The reports will show:
Student ID and Name, Total Average
Course's Name, Teacher's Name and Course's Average
"""
import pandas as pd 

from logic.quality_test import unique_test, weights_test, marks_test
from logic.read_file import read_file
from logic.write_file import write_file


def manage(path_in, path_out):
    courses = read_file(path_in, 'courses')
    marks = read_file(path_in, 'marks')
    students = read_file(path_in, 'students')
    tests = read_file(path_in, 'tests')

    def tests_suite():
    # test input quality, only process if satisfied
        return (unique_test(courses), unique_test(students), unique_test(tests), weights_test(tests), marks_test(marks))

    # join table on unique index
    result = pd.merge(marks, tests, on='test_id')
    result = pd.merge(result, students, on='student_id')
    result = pd.merge(result, courses, on='course_id')
    # beautifying final result
    result = result.sort_values(['student_id', 'course_id'], ascending=True).reset_index().drop('index', axis=1)
    result.rename({'name_x': 'student_name', 'name_y': 'course_name'}, inplace=True, axis='columns')
    result = result.set_index(['student_id', 'student_name', 'course_id', 'course_name', 'teacher'])

    write_file(path_out, result)

    return tests_suite
