import numpy as np
def unique_test(dfs):
    for df in dfs:
        if df.index.unique().values.size == df.index.values.size:
            print('{} unique index test OK...'.format(df.index.name))
            pass
        else:
            print('{} duplicate error!'.format(df.index.name))
            exit()


def weights_test(df):
    for idx in np.unique(df['course_id'].values):
        subject_weights = df[df.course_id == idx]
        if subject_weights['weight'].sum() != 100:
            print('Weight percent error! Check {}.txt file.'.format(df))
            exit()
    print('Weight percent test OK...')


def marks_test(df):
    corrupted_mark = df[df.mark > 100]
    if not corrupted_mark.empty:
        print('Marks corrupt! Check {}.txt file.'.format(df))
        exit()
    print('Mark test OK. All test done!')