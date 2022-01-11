from os import listdir
from os.path import isfile, join
def gen_file_list(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


