import numpy as np 
from logic.file_processor import get_student_data

# write output
def write_file(df):
    with open('reports.txt', 'w+') as f:
        for idx in np.unique(df.index.get_level_values('student_id')):
            report = get_student_data(df,idx)
            student_index = report['id']
            student_name = report['name']
            first_line = '\nStudent Id: {}, name: {}\n'.format(student_index, student_name)
            f.write(first_line)
            starting_point = len(first_line) - len(student_name)
            padding_spaces = (starting_point - len('Total Average: '))*' '
            f.write('Total Average:{0}{1:.2f}%\n\n'.format(padding_spaces, report['total_avg']))
            for course in report['courses_report']:
                course_name = course['course_name']
                teacher = course['teacher']
                course_avg = course['course_avg']
                f.write('    Course: {}, Teacher: {}\n'.format(course_name, teacher))
                padding_spaces = (starting_point - len('    Final Grade: ')) * ' '
                f.write('    Final Grade:{0}{1:.2f}%\n\n'.format(padding_spaces, course_avg))
