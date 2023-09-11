
import random

# Funktio, joka palauttaa satunnaisen nopan silmäluvun 1..6 väliltä
def heita_noppaa():
    return random.randint(1, 6)

# Pääohjelma
if __name__ == "__main__":
    while True:
        silmaluku = heita_noppaa()
        print("Noppa näytti:", silmaluku)
        if silmaluku == 6:
            print("Sait kuutosen! Pelin loppu.")
            break
