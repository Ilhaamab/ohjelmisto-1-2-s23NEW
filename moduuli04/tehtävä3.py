# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
import math

pienin = math.inf
suurin = math.inf

lukuStr = input("Anna kokonaisluku,  tyhjä lopettaa):")

while lukuStr != "":
    luku = int(lukuStr)
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku

else:
    print(f"Suurin luku oli (suurin)")
    print(f"Pienin luku oli (pienin)")

