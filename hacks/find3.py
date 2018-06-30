from pathlib import Path
from sys import argv

_, start, query = argv

start_path = Path(start)

for f in start_path.rglob(query):
    new = open(f)
    lines = new.readline()
    print (lines)
