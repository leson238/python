import pandas as pd

def read_file(path, file_name):
    f = pd.read_csv('{}\\{}.csv'.format(path, file_name), index_col=0)
    id_name = file_name[:-1] + '_' + 'id'
    if f.index.name == 'id':
        f.index.name = id_name
    return f




