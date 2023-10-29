import random

class Auto:
    def __init__(self, nimi, nopeus):
        self.nimi = nimi
        self.nopeus = nopeus
        self.matka = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-5, 5)
            auto.nopeus += nopeuden_muutos
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Nimi':<15}{'Nopeus (km/h)':<15}{'Matka (km)':<15}")
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15}{auto.matka:<15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

# Pääohjelma
if __name__ == "__main__":
    autot = [Auto("Auto 1", 100), Auto("Auto 2", 120), Auto("Auto 3", 110), Auto("Auto 4", 130),
             Auto("Auto 5", 95), Auto("Auto 6", 115), Auto("Auto 7", 105), Auto("Auto 8", 125),
             Auto("Auto 9", 90), Auto("Auto 10", 140)]

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        if tunti % 10 == 0:
            print(f"Tunnin välein tilanne:")
            kilpailu.tulosta_tilanne()
        tunti += 1

    print(f"Kilpailu on päättynyt. Lopputilanne:")
    kilpailu.tulosta_tilanne()
