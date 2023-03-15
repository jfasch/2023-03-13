import sys

filename = sys.argv[1]
f = open(filename)

lines = words = chars = 0

for line in f:
    lines += 1
    chars += len(line)
    words += len(line.split())

print(lines, words, chars, filename)
