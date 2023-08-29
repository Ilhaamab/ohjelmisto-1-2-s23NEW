# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

biologinen_sukupuoli = input("Syötä biologinen sukukupuoli (mies/nainen):")
hemoglobiininarvo = float("Anna hemoglobiininarvo (g/l)")

elif sukupuoli "mies":

if 134 <= hemoglobiini<= 195:
        print("Hemoglobiiniarvo on normaali miehillä.")

elif hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen miehillä.")

else:
        print("Hemoglobiiniarvo on korkea miehillä.")

elif sukupuoli "nainen":

    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali naisilla.")
    elif hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen naisilla.")
    else:
        print("Hemoglobiiniarvo on korkea naisilla.")
else:
    print("Virheellinen syöte. Syötä jokin seuraavista: Mies, Nainen.")


