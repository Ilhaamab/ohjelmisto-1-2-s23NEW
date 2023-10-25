# Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = int(input('Anna kokonaisluku: '))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1+luku2+luku3
tulo = luku1*luku2*luku3
keskiarvo = (luku1+luku2+luku3)/3



print(f'summa on ',summa)
print(f"tulo on",tulo)
print(f"keskiarvo on",(keskiarvo/2))