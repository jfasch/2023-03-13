from stuff import category

def test_basic():
    s = r'Bezahlung Karte MC/000009284|ORPHEUM BAR  2371  K002 28.02. 21:14|ORPHEUM BAR\\GRAZ\8020 ST'
    assert category.categorize(s) == 'luxury'

    s = r'Bezahlung Karte MC/000009278|BILLA 6278   2322  K002 27.02. 18:51|BILLA DANKT\\GRAZ\8010 ST'
    assert category.categorize(s) == "living"

    s = r'Bezahlung Karte MC/000009269|ENI 7104     2140  K002 22.02. 10:56|ENI 7104\\GRAZ\8053 ST 04'
    assert category.categorize(s) == "car"
    


    
