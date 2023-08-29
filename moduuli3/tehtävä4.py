#  Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#  Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#  Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi  = input("Anna vuosi:")

if vuosi % 4 != (vuosi % 100 != 0 tai vuosi % 400 == 0):
    print("Vuosi", vuosi, "on karkausvuosi.")
else:
    print("Vuosi", vuosi, "ei ole karkausvuosi.")