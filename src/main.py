import os
from format import process
from files import gen_file_list
import sys



def main():
    '''
    try:
        process(sys.argv[1])
    except FileNotFoundError as err:
        print(err)
        sys.exit(0)
    '''
    #print('Finished conversion')
    try:
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\tests\\'
        files = gen_file_list(path)
        for f in files:
            process(path+f)
    except FileNotFoundError as err:
        print(err)
        sys.exit(0)

    print('Finished conversion')

if __name__ == '__main__':
    main()
