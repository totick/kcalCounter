"""
Beräknar antalet kalorier man har bränt vid springrunda eller promenad
"""


print("############  Motion  ###########")

avsluta= "nej"

while avsluta != "ja":
    träningstyp=input("ange träningstyp sprang/gick: ")
    if träningstyp=="sprang":
        kaloriPerkm=1
    elif träningstyp == "gick":
        kaloriPerkm=0.7
    else:
        print("Känner inte igen angiven träningstyp. Programmet avslutas")
        raise SystemExit(0)

    vikt = float(input("hur mkt väger du? "))

    antalkilometer = float(input("hur långt " + träningstyp + " du? "))

    resultat=vikt * antalkilometer * kaloriPerkm

    print("Du har bränt", resultat,"kalorier")
    
    avsluta = input("Vill du avsluta (ja/nej)? ")



