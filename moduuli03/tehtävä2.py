hyttiluokka = input("Syötä laivan hyttiluokka: ")

#if hyttiluokka == "LUX" or hyttiluokka = "lux":
#  print("kirjoitit LUX tai lux")

hyttiluokka= str.upper(hyttiluokka)

if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen syöte. Syötä jokin seuraavista: LUX, A, B, C.")