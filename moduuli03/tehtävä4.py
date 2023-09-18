#  Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#  Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#  Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosi:"))

if vuosi % 4 == 0 or (vuosi % 100 == 0 and vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")


else:
    print("Vuosi ei ole karkausvuosi.")

    vuosi = int(input("Anna vuosiluku:"))

    if vuosi % 4 :
        print("Vuosiluku on karkausvuosi", vuosi)

    elif vuosi % 100 and 400:
        print("on karkausvuosi jos on vain näillä jaollinen")
