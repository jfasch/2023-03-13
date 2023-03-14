import sys

if len(sys.argv) != 2:
    print('du doedel, uebergib **eine** zahl!')
    sys.exit(1)

zahl = int(sys.argv[1])
if zahl % 2 != 0:
    print('yay')
else:
    print('nix')
