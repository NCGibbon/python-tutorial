"""Read and print an integer series"""

import sys

def read_series(filename):
    with open(filename, mode='rt', encoding = 'utf-8') as f: #this opens and closes the file
        return [int(line.strip()) for line in f]
    
def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])