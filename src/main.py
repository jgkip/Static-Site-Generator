import os
from format import process
from files import gen_file_list
import sys
import timeit
import time

def main():
    try:
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\tests\\' # change 'tests' to directory where input files are stored
        files = gen_file_list(path)
        for f in files:
            #print(f)
            process(path+f)
    except FileNotFoundError as err:
        print(err)
        sys.exit(0)
    finally:
        print('Finished conversion')
    
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('Time elapsed: ~'+str(round(end-start,3))+'s')
