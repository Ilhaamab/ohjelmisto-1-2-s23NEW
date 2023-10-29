class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.kerros:
            self.kerros_ylos(kohde_kerros)
        elif kohde_kerros < self.kerros:
            self.kerros_alas(kohde_kerros)

    def kerros_ylos(self, kohde_kerros):
        while self.kerros < kohde_kerros and self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f'Hissi on kerroksessa {self.kerros}')

    def kerros_alas(self, kohde_kerros):
        while self.kerros > kohde_kerros and self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f'Hissi on kerroksessa {self.kerros}')


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = []
        for i in range(hissien_lukumaara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Virheellinen hissin numero.")

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

# Pääohjelma
if __name__ == "__main__":
    talo = Talo(1, 10, 2)  # Alin kerros: 1, Ylin kerros: 10, 2 hissiä

    # Ajetaan ensimmäistä hissiä
    talo.aja_hissiä(0, 5)  # Hissi numero 0 siirtyy kerrokseen 5
    talo.aja_hissiä(0, 2)  # Hissi numero 0 siirtyy kerrokseen 2

    # Ajetaan toista hissiä
    talo.aja_hissiä(1, 7)  # Hissi numero 1 siirtyy kerrokseen 7

    # Käynnistetään palohälytys
    print("Palohälytys!")
    talo.palohälytys()
