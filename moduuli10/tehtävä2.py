#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


class Hissi:
    def __init__(self, alin_kerros, ylimm_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimm_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1

class Talo:
    def __init__(self, alin_kerros, ylimm_kerros, hissien_lukumäärä):
        self.hissit = [Hissi(alin_kerros, ylimm_kerros) for _ in range(hissien_lukumäärä)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            hissi = self.hissit[hissi_numero]
            while hissi.kerros < kohde_kerros:
                hissi.kerros_ylös()
            while hissi.kerros > kohde_kerros:
                hissi.kerros_alas()
            return hissi.kerros
        else:
            return None

# Pääohjelma
if __name__ == "__main__":
    talo = Talo(alin_kerros=1, ylimm_kerros=10, hissien_lukumäärä=2)

    for i, hissi in enumerate(talo.hissit):
        print(f"Hissi {i}: Kerros {hissi.kerros}")

    hissi_numero = 1  # Valitse hissi numero
    kohde_kerros = 7  # Valitse kohdekerros
    uusi_kerros = talo.aja_hissiä(hissi_numero, kohde_kerros)

    if uusi_kerros is not None:
        print(f"Hissi {hissi_numero} on kerroksessa {uusi_kerros}")
    else:
        print(f"Virhe: Hissiä numero {hissi_numero} ei löydy.")

    for i, hissi in enumerate(talo.hissit):
        print(f"Hissi {i}: Kerros {hissi.kerros}")