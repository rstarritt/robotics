# Main entry point for the python code
import sys
from data_reader import get_data

def main(argv):
    if len(argv) <= 0:
        print("Usage: python3 main.py training_file1 ... trainingfile_n")
        exit(-1)

    print("Parsing files")
    data = []

    for x in argv:
        data.append(get_data(x))
    
    print(data)

if __name__ == "__main__":
    main(sys.argv[1:])