
def listat(operate):
    list = [15,1,8,18,33]
    borders = (5, 15)
    result = list[3] + borders[0]
    print(f"Sallittujen lukujen summa {result}")

listat(5)


def noppa(calculate):
    number = int(input("Syötä kokonaisluku:"))
    result = calculate * number
    print(f'lukusi 3-kertaisena {result}')


noppa(3)


def tervehdys(nimet):
    nimi = input("Syötä nimi: ")
    print("Hello, " + nimi + "!")

tervehdys('ilhaam')


import random
from random import randint
def cast_dice():
    dice = int(input("Montako noppaa?"))
    faces = random.randint(1, 18)
    result = dice + faces
    return f"silmälukujen summa {result}"

print(cast_dice())