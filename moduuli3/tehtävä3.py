# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.


sukupuoli = input("Syötä biologinen sukukupuoli (mies/nainen):")

hemoglobiininarvo= float(input("Anna hemoglobiininarvo (g/l)"))

if sukupuoli == 'nainen':
    if 117 <= hemoglobiininarvo <= 175:
        print("Hemoglobiiniarvo on normaali")
    elif hemoglobiininarvo < 117:
        print("hemoglobiininarvo alhainen")
    else:
        print("hemoglobiininarvo on korkea")

if sukupuoli == 'mies':
    if 134 <= hemoglobiininarvo <= 195:
        print("Hemoglobiiniarvo on normaali")
    elif  hemoglobiininarvo <= 134:
         print("hemoglobiininarvo alhainen")
    else:
        print("hemoglobiininarvo on korkea")