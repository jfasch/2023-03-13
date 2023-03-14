import sys

# links = 9
# rechts = 77

if len(sys.argv) == 1:
    links = int(input('Bitte gib eine Zahl ein: '))
    rechts = int(input('Bitte gib noch eine Zahl ein: '))
elif len(sys.argv) == 3:
    links = int(sys.argv[1])
    rechts = int(sys.argv[2])
else:
    print('du doedel, null oder zwei ziffern will ich!')
    sys.exit(1)

if links < rechts:
    print(rechts)
elif links > rechts:
    print(links)
else:
    print('jessas, wie soll sich hier wer auskennen!')
