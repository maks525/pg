def sudy_nebo_lichy(hodnota):
    if (hodnota % 2) == 0:
        print(f'cislo {hodnota} je sudy')
    else:
        print(f'cislo {hodnota} je lichy')



if __name__ == '__main__':
    
    cislo = input('Zadejte cislo ')
    cislo = int(cislo)

    print(f'Cislo je: {cislo}')
    
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)
    sudy_nebo_lichy(cislo)