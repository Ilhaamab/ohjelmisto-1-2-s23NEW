#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
#(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
#kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja
#for/in toistorakennetta niiden läpikäymiseen.

# Luodaan tyhjä lista kaupungeille
kaupungit = []

# Käytetään for-silmukkaa viiden kaupungin nimen kysymiseen
for i in range(5):
    kaupunki = input("Syötä kaupungin nimi: ")
    kaupungit.append(kaupunki)  # Lisätään kaupunki listaan

# Tulostetaan kaupunkien nimet yksi kerrallaan
print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)



