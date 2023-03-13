def categorize(s):
    if s.startswith('Bezahlung Karte'):
        which, terminal, organization = s.split('|')

        if organization.startswith('BILLA'):
            return 'living'
        elif organization.startswith('ENI'):
            return 'car'
        elif organization.startswith('ORPHEUM'):
            return 'luxury'
        else:
            return 'card-unknown'
    else:
        return 'unknown'

