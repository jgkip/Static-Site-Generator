import os
from format import process
import sys



def main():
    try:
        process(sys.argv[1])
    except FileNotFoundError as err:
        print(err)
        sys.exit(0)
    print('Finished conversion')



if __name__ == '__main__':
    main()
