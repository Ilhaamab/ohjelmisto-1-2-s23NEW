
numero1 = 5
numero2 = 10
teksti = ("lasketaan matikkaa!")

print(numero1 * numero2)
print(teksti)

# Luo ohjelma, joka tulostaa viestin
# saippuakauppias
print("saippuakauppias")

# Luo ohjelma, joka tulostaa viestin
result = 3+2
print("2+3=",result)

# Luo ohjelma, joka asettaa muuttujaan laskun 3 + 1000 + 5 lopputuloksen,
# ja tulostaa muuttujan arvon. Keksi itse muuttujalle sopiva nimi!

tulos =3+1000+5
print("3+1000+5=",tulos)

# Luo ohjelma, joka asettaa muuttujaan laskun 1084 - 3000 + 4103 lopputuloksen,
# ja tulostaa muuttujan arvon.
# Keksi itse muuttujalle sopiva nimi!
2187
tulos = 1084-3000+4103
print("1084-3000+4103=",tulos)

# Luo ohjelma, joka laskee laskun 60 * 60 * 24, ja tulostaa lopputuloksen seuraavasti:
tulos = 60*60*24
print("60*60*24=",tulos)

#testi
kokonaisluku = 123
print("kokonaislukumuuttuja arvo on" +  str(kokonaisluku))

#testi2
kokonaisluku = int(input("Anna luku:"))
print("luku on ", kokonaisluku )


Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = input("Anna vuosiluku:")

if vuosi % 4:
    print("Vuosiluku on karkausvuosi", vuosi)

elif vuosi % 100 and 400:
    print("on karkausvuosi jos on vain näillä jaollinen")

