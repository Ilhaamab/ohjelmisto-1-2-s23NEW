#Kirjoita ohjelma, joka kysyy käyttäjältä massan
# keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi
# sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiviskat = int(input("Anna leivisköiden määrä: "))
naulat = int(input("Anna naulojen määrä: "))
luodit = float(input("Anna luotien määrä: "))

# muutetaan saadut leviskät, naulat ja luodit grammoiksi
# luotien massa grammoina
luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
paino_kg = koko_luoteina * 13.3 / 1000
paino_gr = koko_luoteina * 13.3 % 1000

# kuinka montakokonaista iloa?
kilot= int(kokonaismassaGr/1000)

# monta grammaa jää yli
print(paino_kg,'ja', paino_gr)