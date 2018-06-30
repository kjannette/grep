from pathlib import Path
from sys import argv
import glob
import re

_, directory, file_type, search_term = argv #file_type has to be in quotes on
                                            #command line, ie
                                            # "*.txt"

start_path = Path(directory)
#search_term = str(term)

for f in start_path.rglob(file_type):
    try:
        for line in open(f, 'r'):
            if re.search(search_term, line): #if re.match(search_term, line):
                print (line)                    #search - anywhere in line
    except:
        print ("Whoopsie daisy")                #match - beginning of line
