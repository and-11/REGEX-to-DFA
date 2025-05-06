
def Cuvant_Valid(cuvant, stare_curenta, relatie, stari_finale):

    if cuvant == "":
        if stare_curenta in stari_finale:
            return 1
        else:
            return 0

    litera = cuvant[0:1]

    if litera not in relatie[stare_curenta]:
        return 0

    for stare_viitoare in relatie[stare_curenta][litera]:
        if Cuvant_Valid(cuvant[1:], stare_viitoare,relatie, stari_finale):
            return 1

    return 0
