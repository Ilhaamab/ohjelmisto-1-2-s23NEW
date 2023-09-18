Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
import random

nimet set ()

nimi = input("Syötä nimi, (tyhjä rivi lopettaa):")

while True
    not nimi:
    break

    if nimi in nimet
        print("Aiemmin syötetyt nimet")



