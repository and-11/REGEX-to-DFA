
def Cuvant_Valid(cuvant, stare_curenta, relatie, stari_finale):

    if cuvant == "":
        if stare_curenta in stari_finale:
            return 1
        else:
            return 0

    # print("-->",cuvant,"  ",stare_curenta,"\n\n") 
    
    litera = cuvant[0:1]

    if litera not in relatie[stare_curenta]:
        return 0

    if litera in relatie[ stare_curenta ] :
        if Cuvant_Valid(cuvant[1:], relatie[ stare_curenta ][litera] ,relatie, stari_finale):
            return 1

    return 0
