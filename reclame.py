from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    korting_prijs = f"{prijs*(1-korting):.2f}".replace(".",",")
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting_prijs}."
print (aanbieding_1("aardbei",4,0.1))
'''
def aanbieding_1(smaak,prijs,korting):
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs*(1-korting):.2f}."
print (aanbieding_1("aardbei",4,0.1))
'''
def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for inkomst in inkomsten:
        totaal += inkomst
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal*btw} euro btw betaald dient te worden."

print(inkomsten_totaal([220,430,125,160,205,90,345],0.09))

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst),min(mijn_lijst)]
print(laag_en_hoog([220,430,125,160,205,90,345]))

def gemiddelde(mijn_lijst):
    totaal = 0
    for inkomst in mijn_lijst:
        totaal += inkomst
    return f"De gemiddelde inkomsten deze week zijn {totaal/len(mijn_lijst)} euro."
print(gemiddelde([220,430,125,160,205,90,345]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
