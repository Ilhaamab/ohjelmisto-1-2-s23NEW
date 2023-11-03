import requests

def hae_saa_tiedot(api_key, paikkakunta):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": paikkakunta,
        "appid": api_key,
        "units": "metric"  # Muunnetaan lämpötila Celsius-asteiksi
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        saa_tila = data["weather"][0]["description"]
        lampotila = data["main"]["temp"]
        return saa_tila, lampotila
    else:
        return None, None

def main():
    api_key = "TÄHÄN_OMA_API_AVAIN"
    paikkakunta = input("Anna paikkakunnan nimi: ")

    saa_tila, lampotila = hae_saa_tiedot(api_key, paikkakunta)

    if saa_tila is not None and lampotila is not None:
        print(f"Sää paikkakunnalla {paikkakunta}: {saa_tila}")
        print(f"Lämpötila: {lampotila} °C")
    else:
        print("Säätilan haku epäonnistui.")

if __name__ == "__main__":
    main()
