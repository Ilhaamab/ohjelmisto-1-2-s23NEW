import mysql.connector

def etsi_kenttätyyppi(iso_country):
    sql = ("""SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY COUNT(*) DESC
    """)
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql, (iso_country,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f'Kentän tyyppi {rivi[0]}:\n Lukumäärä {rivi[1]}')
    return


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Lontoo2023',
         autocommit=True
         )

iso_country = input('Syötä maakodi (FI, US jne): ')
etsi_kenttätyyppi(iso_country)