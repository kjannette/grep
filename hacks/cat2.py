import argparse
parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F', type=str, nargs='+')

args = parser.parse_args()

print (">parsed args: ", args)

with open("hoebag.txt", "w") as outfile:

    for in_file_name in args.files:
        in_file = open(args.files)
        for line in in_file:
            outfile.write(line)
#        in_file2 = open(args.files[1])
#        for line in in_file2:
    #        outfile.write(line)

outfile.close()
