# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti,
# kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin
# Liian suuri arvaus,Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random


oikea_luku = random.randint(1, 10)
arvaukset = 0

while True:
    arvaus = int(input("Arvaa luku väliltä 1..10: "))
    arvaukset += 1

    if arvaus < oikea_luku:
        print("Liian pieni arvaus.")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein! Arvasit luvun", oikea_luku, "arvauskertoja tarvittiin:", arvaukset)
        break
