from sys import argv
from pathlib import Path
import re, glob
import argparse

#python3 sed6.py . "*.txt" a XXXXX -r

def replace(directory, file_type, find, change):
    start_path = Path(directory)
    with open('pig.txt', 'w') as outfile:
        for f in start_path.rglob(file_type):
            for line in open(f, 'r'):
                new_line = re.sub(find, change, line) #this is where you could change
                outfile.write(new_line)             #the re.sub to something else
    outfile.close()                                 #to add other functions

def Main():

    parser = argparse.ArgumentParser()

    parser.add_argument("directory")
    parser.add_argument("file_type")
    parser.add_argument("find")
    parser.add_argument("change")
    parser.add_argument('-r', '--replace', action='store_true')

    args = parser.parse_args()

    if args.replace:
        replace(args.directory, args.file_type, args.find, args.change)
    else:
        print ("no option on command line")

if __name__ == "__main__":
    Main()
