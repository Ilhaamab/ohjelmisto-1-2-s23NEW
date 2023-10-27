# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class auto:
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

uusi_auto = auto("ABC-123", 142)

print("Alkuperäinen nopeus:", uusi_auto.nykyinen_nopeus, "km/h")

uusi_auto.kiihdytä(30)
print("Nopeus kiihdytyksen jälkeen:", uusi_auto.nykyinen_nopeus, "km/h")

uusi_auto.kiihdytä(70)
print("Nopeus kiihdytyksen jälkeen:", uusi_auto.nykyinen_nopeus, "km/h")

uusi_auto.kiihdytä(50)
print("Nopeus kiihdytyksen jälkeen:", uusi_auto.nykyinen_nopeus, "km/h")

# Hätäjarrutus
uusi_auto.kiihdytä(-200)
print("Nopeus hätäjarrutuksen jälkeen:", uusi_auto.nykyinen_nopeus, "km/h")


