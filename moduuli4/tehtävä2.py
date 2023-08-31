# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = float(input('Anna tuumamäärä (negatiivinen luku lopettaa): '))
vastaus = tuumat * 2.54

while tuumat >= 0:
    print(vastaus)
    tuumat = float(input('Anna tuumamäärä (negatiivinen luku lopettaa): '))
    vastaus = tuumat * 2.54

print("Annoit negatiivisen luvun. Ohjelma lopetetaan")
