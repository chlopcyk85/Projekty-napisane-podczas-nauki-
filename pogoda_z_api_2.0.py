import requests
import json
from datetime import datetime, timedelta


class WeatherForecast:
    def __init__(self, latitude, longitude, file_name="pogoda.json"):
        self.latitude = latitude
        self.longitude = longitude
        self.file_name = file_name
        self.data = self.wynik_odczytaj() or {"history": []}

    def wynik_odczytaj(self):
        try:
            with open(self.file_name, "r") as plik:
                data = json.load(plik)
            if data["history"]:
                print(f"\n Pogoda pobrana z pliku {self.file_name}")
                return data
        except FileNotFoundError:
            return None

    def wynik_zapisz(self):
        with open(self.file_name, "w") as plik:
            json.dump(self.data, plik)

    def api(self, date):
        url = (
            f"https://api.open-meteo.com/v1/forecast?latitude="
            f"{self.latitude}&longitude={self.longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date="
            f"{date}&end_date={date}"
        )

        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
            print("Nie pobrano danych o pogodzie na wyznaczony dzień.")

    def __setitem__(self, date, weather):
        self.data["history"].append(weather)
        self.wynik_zapisz()

    def __getitem__(self, date):
        return (item[date] for item in self.data["history"] if date in self.data)

    def __iter__(self):
        yield (date for item in self.data["history"] for date in item.keys())

    def items(self):
        return ((date, self[date]) for date in self)


def main():
    latitude = 50.86
    longitude = 20.62
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    next_day = tomorrow.strftime("%Y-%m-%d")

    miasto = input(
        """\nWybierz miasto dla którego chcesz sprawdzić pogodę:
    * Warszawa
    * Kraków
    * Wrocław
    Miasto: """
    ).lower()

    if miasto == "warszawa":
        latitude = 52.22
        longitude = 21.01
    elif miasto == "kraków" or miasto == "krakow":
        latitude = 50.04
        longitude = 19.94
    elif miasto == "wrocław" or miasto == "wroclaw":
        latitude = 51.10
        longitude = 17.03
    else:
        print("Nie mamy takiego miasta w bazie!")

    if not miasto:
        print("Brak podania miasta, zostanie pobrana pogoda dla miasta Kielce")

    searched_date = input(
        f"\n - Podaj dzień na który mam sprawdzić pogodę {miasto}, np. 2023-11-03: "
    )
    if not searched_date:
        print(
            f"\n - Brak podania daty, została pobrana pogoda na dzień jutrzejszy tj. {next_day}"
        )
        searched_date = next_day

    weather_forecast = WeatherForecast(latitude, longitude)
    data = weather_forecast.api(searched_date)
    if data is not None:
        weather_forecast[searched_date] = data
        rain_sum = data["daily"]["rain_sum"]
        rain_sum = sum(rain_sum)

        print(
            "* Będzie padać :( * "
            if rain_sum > 0
            else " * Nie będzie padać :) * "
            if rain_sum == 0
            else "Nie wiem."
        )


if __name__ == "__main__":
    main()
