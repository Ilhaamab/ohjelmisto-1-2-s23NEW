#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
#(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
#kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja
#for/in toistorakennetta niiden läpikäymiseen.

# Luodaan tyhjä lista kaupungeille
kaupungit = []
i = 1

for i in range(5):
    kysy_kaupungit = str(input('Lisää viisi kaupunkia:'))
    kaupungit.append('kysy_kaupungit:')
    i += 1

    print ("Tässä lisäämäsi kaupungit:")
    j=1
    while j <= 5:
        for kaupunki in kysy_kaupungit:
            print(f'{j}:{kysy_kaupungit}\n')
            j += 1



