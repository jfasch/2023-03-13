import sys

number = int(sys.argv[1])

if number == 1:
    print(number, 'ist ganz sicher keine Primzahl, da brauch ich nicht drueber nachzudenken')
    sys.exit()

if number <= 0:
    print(number, 'kann ich nix sagen zu, denn die ist nicht in der Definitionsmenge')
    sys.exit(1)


for divisor_candidate in range(2, number//2 + 1):
    if number % divisor_candidate == 0:     # wenn divisor_candidate ein teiler von number ist
        print(number, 'is not prime')
        break
else:
    print(number, 'is prime')
