import sys

if len(sys.argv) == 1:
    links = int(input('Bitte gib eine Zahl ein: '))
    rechts = int(input('Bitte gib noch eine Zahl ein: '))
elif len(sys.argv) == 3:
    links = int(sys.argv[1])
    rechts = int(sys.argv[2])
else:
    print('du doedel, null oder zwei ziffern will ich!')
    sys.exit(1)

def maximum(a, b):
    'Takes two integers a and b, and returns the maximum of them'
    if a < b:
        return b
    return a

m = maximum(links, rechts)
print(m)

