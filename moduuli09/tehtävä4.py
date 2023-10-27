#Nyt ohjelmoidaan autokilpailu.Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
#Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.matka += self.nopeus


def luo_autot():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)
    return autot


def kilpailu(autot):
    tunti = 0
    while True:
        tunti += 1
        print(f"Kilpailun tunti {tunti}:\n")
        for auto in autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje()
            print(f"{auto.rekisteritunnus}: Nopeus {auto.nopeus} km/h, Matka {auto.matka} km")
        print("\n")

        voittaja = None
        for auto in autot:
            if auto.matka >= 10000:
                voittaja = auto
                break

        if voittaja:
            print(f"Voittaja: {voittaja.rekisteritunnus}")
            break


def tulosta_tulokset(autot):
    print("Kilpailun tulokset:\n")
    for auto in autot:
        print(f"{auto.rekisteritunnus}: Huippunopeus {auto.huippunopeus} km/h, Matka {auto.matka} km")


if __name__ == "__main__":
    autot = luo_autot()
    kilpailu(autot)
    tulosta_tulokset(autot)
