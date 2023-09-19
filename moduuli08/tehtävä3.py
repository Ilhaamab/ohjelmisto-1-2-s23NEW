import mysql.connector
from geopy.distance
import geodesic

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

airport1 = input('Enter the ICAO-codeof first airport:')
airport2 = input('Enter the ICAO-code of the second airport:')
distance = geodesic(args; search_airport(airport1),search_airport(airport2)).kilometers

print(f'The distance between the airports is(distance:.0f) kilometers.')