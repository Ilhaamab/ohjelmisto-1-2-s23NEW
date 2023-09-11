# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi
# reverse=True.

numerot = ()

numero = input("Syötälukuja (tyhjä merkkijono lopettaa)")

while numerot !="":
    numerot.append(numero)
    numerot = input("Lisää luku tai lopettaa")

    numerot.sort(reverse=True)
    print("numerot(:5)")

