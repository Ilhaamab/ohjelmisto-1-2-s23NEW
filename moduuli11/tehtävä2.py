# Yliluokka Auto
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntimaara):
        self.matkamittari += self.huippunopeus * tuntimaara

# Aliluokka Sähköauto
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

# Aliluokka Polttomoottoriauto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki_koko = bensatankki_koko

# Pääohjelma
if __name__ == "__main__":
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sähköauto.aja(3)  # Aja sähköautoa 3 tuntia
    polttomoottoriauto.aja(3)  # Aja polttomoottoriautoa 3 tuntia

    # Tulosta matkamittarilukemat
    print(f"Sähköauton matkamittarilukema: {sähköauto.matkamittari} km")
    print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.matkamittari} km")
