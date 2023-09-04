# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules)
oikea_kayttajatunnus = "python"
oikea_salasana = "rules"
yritykset = 5

while yritykset > 0:
    tunnus = input("Mikä on oikea k.tunnus? ")
    salasana = input("Mikä on oikea salasana? ")

    if tunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break

    elif tunnus != oikea_kayttajatunnus and salasana != oikea_salasana:
        print("Väärä käyttäjätunnus tai salasana. Yrityksiä jäljellä:", yritykset - 1)
        yritykset -= 1

else:
    print("Pääsy kielletty. Liian monta yritystä.")
