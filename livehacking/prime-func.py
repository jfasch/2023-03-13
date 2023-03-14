import sys

def is_prime(num):
    '''Given a parameter (an integer >= 1), detects the primeness of it.

    Returns True is num is prime, else False
    Raises RuntimeError if blah blah
    '''
    
    if num == 1:
        return False
    
    if num <= 0:   # user IQ underflow
        raise RuntimeError('kann ich nix sagen zu, denn die ist nicht in der Definitionsmenge')

    for divisor_candidate in range(2, num//2 + 1):
        if num % divisor_candidate == 0:     # wenn divisor_candidate ein teiler von number ist
            return False
    else:
        return True


    
number = int(sys.argv[1])

try:
    if is_prime(number):
        print(number, 'is prime')
    else:
        print(number, 'is not prime')
except RuntimeError:
    print(f'''Du bitte, ueberleg nochmal, ob {number} ueberhaupt im
    Definitionsbereich von Primzahlen liegt.  Falls du nicht weisst,
    wie Primzahlen definiert sind, oder dir nicht klar ist, was eine
    Definitionsmenge ist, geh bitte zurueck auf das letzte Feld.''')
