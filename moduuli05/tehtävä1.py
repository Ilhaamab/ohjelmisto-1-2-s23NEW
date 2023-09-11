# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
import random

lukumäärä = int(input("Mikä on arpakuutioiden määrä?"))

summa = 0

for luku in range(lukumäärä):
    luku = random.randint(1,6)
    print(f"Heitto: (silmäluku)")
    summa += lukumäärä

    print("Kaikkien heittojen summa:(summa)")

