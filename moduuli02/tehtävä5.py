leiviskat = int(input("Anna leivisköiden määrä: "))
naulat = int(input("Anna naulojen määrä: "))
luodit = float(input("Anna luotien määrä: "))

koko_luoteina = (leiviskat * 20 * 32) + (naulat * 32) + luodit
paino_kg = koko_luoteina * 13.3 / 1000
paino_gr = koko_luoteina * 13.3 % 1000


print(paino_kg,'ja', paino_gr)