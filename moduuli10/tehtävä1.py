#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
# ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.


class Hissi:

    def __init__(self):
        self.kerros = alin_kerros
        self.kerros_alin = kerros_alin
        self.kerros_ylin = kerros_ylin

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        return self.kerros

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        return self.kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros < kohde_kerros:
            self.kerros_ylös()
        while self.kerros > kohde_kerros:
            self.kerros_alas()
        return self.kerros

    # Testaa Hissi-luokkaa
    if __name__ == "__main__":
        hissi = Hissi(alin_kerros=1, ylimm_kerros=10)

        print(f"Hissi on alimmassa kerroksessa: {hissi.kerros}")

        kohde_kerros = 5
        hissi.siirry_kerrokseen(kohde_kerros)
        print(f"Hissi on kerroksessa {kohde_kerros}: {hissi.kerros}")

        hissi.siirry_kerrokseen(hissi.alin_kerros)
        print(f"Hissi on palannut alimpaan kerrokseen: {hissi.kerros}"