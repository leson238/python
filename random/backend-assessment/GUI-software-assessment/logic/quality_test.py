import numpy as np


def unique_test(df):
    if df.index.unique().values.size == df.index.values.size:
        return '{} unique index test OK...'.format(df.index.name)
    else:
        return '{} duplicate error!'.format(df.index.name)

def weights_test(df):
    for idx in np.unique(df['course_id'].values):
        subject_weights = df[df.course_id == idx]
        if subject_weights['weight'].sum() != 100:
            return 'Weight percent error! Check {}.txt file.'.format(df)
    return 'Weight percent test OK...'


def marks_test(df):
    corrupted_mark = df[df.mark > 100]
    if not corrupted_mark.empty:
        return 'Marks corrupt! Check {}.txt file.'.format(df)
    return 'Mark test OK... All test done!'



