import sys

filename = sys.argv[1]

f = open(filename)

for line in f:
    orig_line = line

    line = line.strip()
    if len(line) == 0:
        continue
    if line[0] == '#':
        continue

    print(orig_line, end='')
