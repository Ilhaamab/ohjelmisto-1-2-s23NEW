#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.


vuodenaika = ("kevät","kesä","syksy","talvi")
järjestysnumerot = int(input("Anna vuodenaika järjestysnumero (1-4): "))
vuodenaika = vuodenaika[järjestysnumerot -1]
print (f"{järjestysnumerot}. vuodenaika on {vuodenaika}.")
