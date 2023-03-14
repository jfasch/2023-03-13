import sys

digit = sys.argv[1]
digit = int(digit)

if digit > 0 or digit < 0:
    print('du doedel, das ist keine ziffer')
    sys.exit(42)

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

translation = translation_table[digit]
print(translation)
