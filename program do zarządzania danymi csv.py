import csv
import sys


# odczyt pliku w formacie .csv
def odczyt_pliku(nazwa_pliku):
    try:
        dane = []
        with open(nazwa_pliku, "r", newline="") as plik:
            reader = csv.reader(plik, delimiter=";")
            for row in reader:
                dane.append(row)
        return dane
    except FileNotFoundError:
        print(f"Nie znaleziono pliku wejściowego {nazwa_pliku}")
        sys.exit(1)


# zmiany w pliku na nowe argumenty
def zmiany_w_pliku(dane, zmiany):
    try:
        try:
            for zmiana in zmiany:
                x, y, value = zmiana.split(",")
                x, y = int(x), int(y)
                dane[x][y] = value
        except TypeError:
            print("Podano złe argumenty")
    except ValueError:
        print("Złe argumenty, dane nie zostały zmienione!")
        sys.exit(1)
    except IndexError:
        print("\nZły INDEX argumentu, dane nie zostały zmienione!\n")


# zapis pliku .csv do nazwy podanej w argumencie
def zapis_pliku(nazwa_pliku, dane):
    try:
        with open(nazwa_pliku, "w", newline="") as plik:
            writer = csv.writer(plik)
            for row in dane:
                writer.writerow(row)
    except TypeError:
        print("Podano złe argumenty do zapisu pliku")


if len(sys.argv) < 2:
    print("Nieprawidłowa ilość argumentów, dane nie zostały zmienione")
    sys.exit(1)

# pobranie argumentów przez terminal
plik_wejscia = sys.argv[1]
plik_wyjscia = sys.argv[2]
zmiany = sys.argv[3:]

# główne operacje
dane = odczyt_pliku(plik_wejscia)
zmiany_w_pliku(dane, zmiany)
zapis_pliku(plik_wyjscia, dane)

# wyświetlanie nowej zawartości
try:
    for line in dane:
        print(" ".join(line))
except TypeError:
    print("Błąd")
