def cislo_text(cislo):
    jednotky = {  0: 'nula', 1: 'jedna', 2: 'dva', 3: 'tři', 4: 'čtyři',
                  5: 'pět', 6: 'šest', 7: 'sedm', 8: 'osm', 9: 'devět',
                 10: 'deset', 11: 'jedenáct', 12: 'dvanáct', 13: 'třináct',
                 14: 'čtrnáct', 15: 'patnáct', 16: 'šestnáct', 17: 'sedmnáct',
                 18: 'osmnáct', 19: 'devatenáct' }
    desitky = { 20: 'dvacet', 30: 'třicet', 40: 'čtyřicet', 50: 'padesát',
                60: 'šedesát', 70: 'sedmdesát', 80: 'osmdesát', 90: 'devadesát' }
    
    
    
    if cislo < 20:
        return jednotky[cislo]
    elif cislo < 100:
        des = (cislo // 10) * 10 
        jed = cislo % 10 
        if jed == 0:
            return desitky[des]
        else: 
            return desitky[des] + ' ' + jednotky[jed]
    else:
        return 'Jenom cisla mensi nez 100, skus to znovu.'
    
    

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)