class Uczen:
    def __init__(self, nazwa, klasa):
        self.nazwa = nazwa
        self.klasa = klasa


class Nauczyciel:
    def __init__(self, nazwa, przedmiot, klasy):
        self.nazwa = nazwa
        self.przedmiot = przedmiot
        self.klasy = klasy


class Wychowawca:
    def __init__(self, nazwa, klasa):
        self.nazwa = nazwa
        self.klasa = klasa


uczniowie = []
nauczyciele = []
wychowawcy = []
klasy = []


# tworzenie ucznia
def stworz_uczen():
    nazwa = input("Wprowadź imię i nazwisko ucznia: ")
    klasa = input("Podaj klasę (np '3c') : ")
    uczen = Uczen(nazwa, klasa)
    uczniowie.append(uczen)
    print(f"Uczeń: {nazwa} został poprawnie dodany. ")


# tworzenie nauczyciela
def stworz_nauczyciel():
    nazwa = input("Podaj imię i nazwisko nauczyciela: ")
    przedmiot = input("Podaj nazwę prowadzonego przedmiotu: ")
    klasy = []

    while True:
        klasa = input(
            "Wprowadź jakie Klasy prowadzi nauczyciel, żeby zakończyć wprowadź pustą linie: "
        )
        if klasa:
            klasy.append(klasa)
        else:
            break
    nauczyciel = Nauczyciel(nazwa, przedmiot, klasy)
    nauczyciele.append(nauczyciel)
    print(f"\nNauczyciel: {nazwa} został poprawnie dodany. ")


# tworzenie wychowawcy
def stworz_wychowawca():
    nazwa = input("Wprowadź imię i nazwisko wychowawcy: ")
    klasa = input("Wprowadź którą Klasę prowadzi Wychowawca: ")
    wychowawca = Wychowawca(nazwa, klasa)
    wychowawcy.append(wychowawca)
    print(f"\nWychowawca {nazwa}, został poprawnie dodany. ")


# funkcja zarządzania użytkownikami
def zarzadzanie():
    while True:
        print("\nZarządzanie użytkownikami\n")
        opcja = input(
            """Prosze wpisać opcję, którą chcesz wybrać (1-5): 
        1 - Klasa
        2 - Uczeń
        3 - Nauczyciel
        4 - Wychowawca
        5 - Koniec
        Komenda: """
        )
        if opcja == "1":
            for uczen in uczniowie:
                print(f"Mamy klasy takie jak: {uczen.klasa}")
            klasa = input("Która klasa Cię interesuje? ")
            print(f"Uczniowie w klasie {klasa}: ")
            for uczen in uczniowie:
                if uczen.klasa == klasa:
                    print(uczen.nazwa)
                for wychowawca in wychowawcy:
                    if wychowawca.klasa == klasa:
                        print(f"Wychowawcą tej klasy jest: {wychowawca.nazwa}")
                    else:
                        print("Klasa nie ma wychowawcy")

        elif opcja == "2":
            for uczen in uczniowie:
                print(f"Mamy uczniów takich jak: {uczen.nazwa}")
            nazwa = input("Podaj imię i nazwisko ucznia: ")
            if nazwa == uczen.nazwa:
                print(f"Uczeń: {uczen.klasa}")
                for nauczyciel in nauczyciele:
                    if uczen.klasa in nauczyciel.klasy:
                        print(
                            f"Ma lekcje takie jak: {nauczyciel.przedmiot} z {nauczyciel.nazwa}"
                        )
            else:
                print("Nie ma takiego ucznia!")
        elif opcja == "3":
            for nauczyciel in nauczyciele:
                print(f"Mamy takich nauczycieli jak: {nauczyciel.nazwa}")
            nazwa = input("Podaj imię i nazwisko nauczyciela: ")
            if nazwa == nauczyciel.nazwa:
                print(f"Nauczyciel: {nauczyciel.nazwa}")
                for klasy in nauczyciel.klasy:
                    print(f"Prowadzi klasy takie jak: {klasy}")
            else:
                print("Nie ma takiego nauczyciela!")
        elif opcja == "4":
            for wychowawca in wychowawcy:
                print(f"Mamy takich wychowawców jak: {wychowawca.nazwa}")
            nazwa = input("Podaj imię i nazwisko wychowawcy: ")
            if nazwa == wychowawca.nazwa:
                print(f"\nWychowawca: {wychowawca.nazwa}\n")
                print(f"Prowadzi uczniów takich jak: ")
                for uczen in uczniowie:
                    if uczen.klasa == wychowawca.klasa:
                        print(uczen.nazwa)
            else:
                print("Nie ma takiego wychowawcy!")
        elif opcja == "5":
            break
        else:
            print("Zła komenda")


print("\nWitamy w programie do zarządzania bazą szkolną \n")
# główne menu
while True:
    wybor = input(
        """Wybierz polecenie (1-3):
         1 - Utwórz użytkownika 
         2 - Zarządzaj użytkownikami
         3 - Koniec 
         Komenda: """
    )
    if wybor == "1":
        polecenie = input(
            """Wybierz jakiego rodzaju użytkownika chcesz utworzyć (1-4):
                1 - Uczeń
                2 - Nauczyciel
                3 - Wychowawca
                4 - koniec 
                Komenda: """
        )
        if polecenie == "1":
            stworz_uczen()
        elif polecenie == "2":
            stworz_nauczyciel()
        elif polecenie == "3":
            stworz_wychowawca()
        elif polecenie == "4":
            continue
        else:
            print("Nie wybrałeś poprawnej opcji")
    elif wybor == "2":
        zarzadzanie()

    elif wybor == "3":
        break
    else:
        print("Nic nie wybrałeś")
