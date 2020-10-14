import pandas as pd
import numpy as np


# squeezing information
def get_course_avg(course_idx, record):
    course_avg = record.apply(lambda x: x['mark'] * x['weight'] / 100, axis=1).sum()
    return course_avg


def get_course_report(course_idx, record):
    course_record = record.xs(course_idx, level='course_id')
    course_name = course_record.index.get_level_values('course_name').values[0]
    teacher = course_record.index.get_level_values('teacher').values[0]
    course_avg = get_course_avg(course_idx, course_record)
    return {
        'course_name': course_name,
        'teacher': teacher,
        'course_avg': course_avg
    }


def get_student_data(df, idx):
    record = df.xs(idx)
    name = record.index.get_level_values('student_name').values[0]
    courses_report = [get_course_report(index, record) for index in np.unique(record.index.get_level_values('course_id'))]
    total_avg = sum([x['course_avg'] for x in courses_report])/len(courses_report)
    return {
        'name': name,
        'id': idx,
        'total_avg': total_avg,
        'courses_report': courses_report
        }