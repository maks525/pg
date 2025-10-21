def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    else:
        for i in range(2, int(cislo ** 0.5) + 1):
            if cislo % i == 0:
                return False
        return True


def vrat_prvocisla(maximum):
    result = []
    for i in range(1, int(maximum) + 1):
        if je_prvocislo(i):
            result.append(i)
    return result

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)