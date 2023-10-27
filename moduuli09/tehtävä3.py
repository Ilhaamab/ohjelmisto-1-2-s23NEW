# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        etenyt_matka = self.nykyinen_nopeus * tuntimaara
        self.kuljettu_matka += etenyt_matka

# Luodaan uusi auto ja asetetaan rekisteritunnus ja huippunopeus parametreina
uusi_auto = Auto("ABC-123", 142)


print("Alkuperäinen nopeus:", uusi_auto.nykyinen_nopeus, "km/h")
print("Alkuperäinen kuljettu matka:", uusi_auto.kuljettu_matka, "km")

uusi_auto.kiihdytä(30)
print("Nopeus kiihdytyksen jälkeen:", uusi_auto.nykyinen_nopeus, "km/h")

uusi_auto.kiihdytä(70)
print("Nopeus kiihdytyksen jälkeen:", uusi_auto.nykyinen_nopeus, "km/h")

uusi_auto.kiihdytä(50)
print("Nopeus kiihdytyksen jälkeen:", uusi_auto.nykyinen_nopeus, "km/h")

uusi_auto.kulje(1.5)
print("Kuljettu matka kulkemisen jälkeen:", uusi_auto.kuljettu_matka, "km")