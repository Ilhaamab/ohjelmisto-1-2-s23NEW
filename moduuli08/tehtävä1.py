# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
# ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.


import mysql.connector


def etsi_lentokenttä(ident):
    sql = ("SELECT name, iso_country FROM airport WHERE ident = %s")
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql, (ident,))
    tulos = kursori.fetchall()
    if kursori.rowcount == 1:
        for rivi in tulos:
            print(f'Syöttämäsi ICAO-koodi on {rivi[0]} ja se sijaitsee maassa {rivi[1]}.')
    return


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='demo_game',
         user='root',
         password='Lontoo2023',
         autocommit=True
         )

icao = input('Syötä ICAO-koodi: ')
etsi_lentokenttä(icao)
