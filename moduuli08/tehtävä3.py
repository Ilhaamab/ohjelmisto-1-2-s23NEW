import mysql.connestor
from geopy.distanceimport goodesic

def search_airport(ident):
    sql="SELECT latitude_deg, longitude_deg FROM airport WEHERIDENT = %S;"
    cursor = connection.cursor()
    lat,long = result = cursor.fetchone ()
    return lat,long

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Lontoo2023',
         autocommit=True

