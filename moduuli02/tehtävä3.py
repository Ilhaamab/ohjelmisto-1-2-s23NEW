#  Ohjelma tulostaa suorakulmion piirin ja
#  pinta-alan. Suorakulmion piiri tarkoittaa
#  sen neljän sivun yhteispituutta.

import math

kanta = float(input("Mikä on suorakulmion kanta? "))
korkeus = float(input("Mikä on suorakulmion korkeus? "))

piiri = 2*(kanta+korkeus)
pinta_ala = kanta*korkeus

print("suorakulmion piiri on",piiri)
print("suorakulmion pinta-ala on",pinta_ala)
