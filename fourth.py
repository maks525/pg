def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):


    typ = figurka["typ"]
    start = figurka["pozice"]
    cil = cilova_pozice
    r1, c1 = start[0], start[1]
    r2, c2 = cilova_pozice[0], cilova_pozice[1]
    if (r1 < 1 or r1 > 8) or (c1 < 1 or c1 > 8):
        return False
    if (r2 < 1 or r2 > 8) or (c2 < 1 or c2 > 8):
        return False
    if start == cil:
        return False
    if cil in obsazene_pozice:
        return False
    dr = r2 - r1
    dc = c2 - c1
    adr = abs(dr)
    adc = abs(dc)
    if typ == "pěšec":
        mezikrok = (r1 + 1, c1)
        if dr <= 0:
            return False
        elif dc != 0:
            return False
        elif dr == 1 and dc == 0:
            return True
        elif dr == 2 and mezikrok not in obsazene_pozice and start[0] == 1:
            return True
        else:
            return False
    elif typ == "jezdec":
        if {adr, adc} =={1, 2}:
            return True
        else:
            return False
    elif typ == "věž":
        if adc == 0 and adr !=0:
            if dr > 0:
                #adr += 1
                while start[0] != cil[0]:
                    adr+=1
                    if adr == obsazene_pozice[0]:
                        return False
                    else:
                        return True
            else:
                while start[0] != cil[0]:
                    adr -= 1
                    if adr == obsazene_pozice[0]:
                        return False
                    else:
                        return True
        elif adr == 0 and adc !=0:
            if dc>0:
                while (start[1] != cil[1]):
                    adc += 1
                    if (adc == obsazene_pozice[1]):
                        return False
                    else:
                        return True
            else:
                while start[1] != cil[1]:
                    adc -= 1
                    if adc == obsazene_pozice[1]:
                        return False
                    else:
                        return True
        else:
            return False

        # start_position = (x, y)
        # valid_move = true
        # end_position = (x2, y2)

        # Move is valid if
        # (x == x2 OR y == y2) AND no_pieces_in_between


        # matched_axis = X
        # axis = "X" // 1
        # axis = "Y" // 2
        # array_of_pieces = [ ("rook", 0, 0) , ("bishop", 5, 0), ("knight", 0, 7)]

        # # GoPositive == GoRight or GoUp
        # for piece in array_of_pieces
        #     if matched_start == matched_end and !(piece[axis] < matched_end and piece(axis) > matched_start)
        #
        # # GoNegative == GoLeft or GoDOwn
        # for piece in array_of_pieces
        #     if matched_start == matched_end and !(piece[axis] < matched_end and piece(axis) > matched_start)
        # # while ()

        # GoLeft
        for figurka in obsazene_pozice:
            if start == cil and not (r1 < r2 and c1 > c2):
                return True
            else:
                return False
        for figurka in obsazene_pozice:
            if start == cil and not (c1 < c2 and r1 > r2):
                return True
            else:
                return False


        # while positions != cil:
        #     for i in range(dr):
        #
        #         start[0] +=1
        #
        #     positions = (positions, positions + 1)
        #     if positions in obsazene_pozice:
        #         return False
        #     elif positions == cil:
        #         return True
    elif typ == "střelec":
        if adr != 0 and adc != 0:
            if adr==adc and dr>0 and dc>0:
                adr+=1
                adc+=1
            elif adr==adc and dr<0 and dc<0:
                adr-=1
                adc-=1
            elif adr == adc and dc > 0 > dr:
                adr-=1
                adc+=1
            elif adr == adc and dc < 0 < dr:
                adr+=1
                adc-=1
            else:
                return False
        else:
            return False




    # elif typ == "dáma":

    elif typ == "král":
        if max(adr, adc) == 1:
            return True
        else:
            return False

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)} #rook
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (5, 8)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2),
                       obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4),
                       obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))
    print(je_tah_mozny(vez, (3, 8), obsazene_pozice))
    # True
    print(je_tah_mozny(strelec, (3, 6), obsazene_pozice))