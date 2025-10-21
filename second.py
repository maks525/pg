def cislo_text(cislo):
    jednotky = {  0: 'nula', 1: 'jedna', 2: 'dva', 3: 'tři', 4: 'čtyři',
                  5: 'pět', 6: 'šest', 7: 'sedm', 8: 'osm', 9: 'devět',
                 10: 'deset', 11: 'jedenáct', 12: 'dvanáct', 13: 'třináct',
                 14: 'čtrnáct', 15: 'patnáct', 16: 'šestnáct', 17: 'sedmnáct',
                 18: 'osmnáct', 19: 'devatenáct' }
    desitky = { 20: 'dvacet', 30: 'třicet', 40: 'čtyřicet', 50: 'padesát',
                60: 'šedesát', 70: 'sedmdesát', 80: 'osmdesát', 90: 'devadesát' }
    setiny = {100: 'sto', 200: 'dve ste', 300: 'tri sta', 400: 'ctyri sta', 500: 'pet set',
              600: 'sest set', 700: 'sedm set', 800: 'osm set', 900: 'devet set'}
    
    
    
    if cislo < 20:
        return jednotky[cislo]
    elif cislo < 100:
        des = (cislo // 10) * 10 
        jed = cislo % 10 
        if jed == 0:
            return desitky[des]
        else: 
            return desitky[des] + ' ' + jednotky[jed]
    elif cislo == 100:
        return setiny[100]
    else:
        return 'Jenom cisla mensi nez 100, skus to znovu.'
    
    

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)