import requests
import json
from datetime import datetime, timedelta


def api(searched_date, latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude="
        f"{latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date="
        f"{searched_date}&end_date={searched_date}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        print("Nie pobrano danych o pogodzie na wyznaczony dzień.")


def pogoda(data):
    rain_sum = data["daily"]["rain_sum"]
    rain_sum = sum(rain_sum)
    if rain_sum > 0:
        print("* Będzie padać :( * ")
    elif rain_sum == 0:
        print(" * Nie będzie padać :) * ")
    else:
        print("Nie wiem.")


def wynik_zapisz(data, file_name):
    with open(file_name, "w") as plik:
        json.dump(data, plik)


def wynik_odczytaj(file_name):
    try:
        with open(file_name, "r") as plik:
            data = json.load(plik)

        if data["history"]:
            print(f"\n Pogoda pobrana z pliku {file_name}")
            return data
    except FileNotFoundError:
        return None


def dodaj_json(data_to_add, file_name):
    existing_data = wynik_odczytaj(file_name)
    if existing_data:
        existing_data["history"].append(data_to_add)
    else:
        existing_data = {"history": [data_to_add]}

    wynik_zapisz(existing_data, file_name)
    print("Wynik został dodany do pliku 'pogoda.json'")


def main():
    latitude = 50.866077
    longitude = 20.628569
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    next_day = tomorrow.strftime("%Y-%m-%d")
    searched_date = input(
        "\n - Podaj dzień na który mam sprawdzić pogodę (miasto Kielce), np. 2023-11-03: "
    )
    if not searched_date:
        print(
            f"\n - Brak podania daty, została pobrana pogoda na dzień jutrzejszy tj. {next_day}"
        )
        searched_date = next_day

    data = api(searched_date, latitude, longitude)
    # wynik_odczytaj("pogoda.json")
    pogoda(data)
    dodaj_json(data, "pogoda.json")


if __name__ == "__main__":
    main()
