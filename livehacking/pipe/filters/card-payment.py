def transform(data):
    data['card_payment'] = data['info'].str.startswith('Bezahlung Karte')
    return data
