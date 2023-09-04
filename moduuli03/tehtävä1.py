# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhan_pituus = int(input("Mikä on kuhan pituus (cm)?"))

if kuhan_pituus <=37:
    puuttuva = 37-kuhan_pituus
    print(f"kuhan pituus on alamittainen, laske se veteen")

else:
    print("kuhan pituus on ylimittainen ")











