uczniowie = {}
nauczyciele = {}
wychowawcy = {}
klasy = []


# tworzenie ucznia
def stworz_uczen():
    uczen = input("Wprowadź imię i nazwisko ucznia: ")
    klasa = input("Podaj klasę (np '3c') : ")
    uczniowie[uczen] = klasa


# tworzenie nauczyciela
def stworz_nauczyciel():
    nauczyciel = input("Podaj imię i nazwisko nauczyciela: ")
    przedmiot = input("Podaj nazwę prowadzonego przedmiotu: ")
    global klasy
    global nauczyciele
    while True:
        klasa = input(
            "Wprowadź jakie Klasy prowadzi nauczyciel, żeby zakończyć wprowadź pustą linie: "
        )
        if klasa:
            klasy.append(klasa)
        else:
            break
    nauczyciele[nauczyciel] = {"przedmiot": przedmiot, "klasy": klasy}


# tworzenie wychowawcy
def stworz_wychowawca():
    global wychowawcy
    wychowawca = input("Wprowadź imię i nazwisko wychowawcy: ")
    klasa = input("Wprowadź którą Klasę prowadzi Wychowawca: ")
    wychowawcy[wychowawca] = klasa


# funkcja zarządzania użytkownikami
def zarzadzanie():
    while True:
        global uczniowie
        global nauczyciele
        global wychowawcy
        global klasy
        print("\nZarządzanie użytkownikami\n")
        opcja = input(
            """Prosze wpisać opcję, którą chcesz wybrać: 
        1 - Klasa
        2 - Uczeń
        3 - Nauczyciel
        4 - Wychowawca
        5 - Koniec
        Komenda: """
        )
        if opcja == "1":
            klasa = input("Która klasa Cię interesuje? ")
            print(f"Uczniowie w klasie {klasa}: ")
            for uczen, ucznie in uczniowie.items():
                if ucznie == klasa:
                    print(uczen)
                for wychowawca, grupy in wychowawcy.items():
                    if klasa in grupy:
                        print(f"Wychowawcą tej klasy jest: {wychowawca}")
                    else:
                        print("Klasa nie ma wychowawcy")

        elif opcja == "2":
            uczen = input("Podaj imię i nazwisko ucznia: ")
            if uczen in uczniowie:
                print(f"Uczeń: {uczen}")
                for nauczyciel, klasy in nauczyciele.items():
                    if uczniowie[uczen] in klasy["klasy"]:
                        print(
                            f"Ma lekcje takie jak: {klasy['przedmiot']} z {nauczyciel}"
                        )
            else:
                print("Nie ma takiego ucznia!")
        elif opcja == "3":
            nauczyciel = input("Podaj imię i nazwisko nauczyciela: ")
            if nauczyciel in nauczyciele:
                print(f"Nauczyciel: {nauczyciel}")
                for klasy in nauczyciele[nauczyciel]["klasy"]:
                    print(f"Prowadzi klasy takie jak: {klasy}")
            else:
                print("Nie ma takiego nauczyciela!")
        elif opcja == "4":
            for wychowawca, klasy in wychowawcy.items():
                print(f"Mamy takich wychowawców jak: {wychowawca}")
            wychowawca = input("Podaj imię i nazwisko wychowawcy: ")
            if wychowawca in wychowawcy:
                klasy_wychowawcy = wychowawcy[wychowawca]
                print(f"\nWychowawca: {wychowawca}\n")
                print(f"Prowadzi uczniów takich jak: ")
                for uczen, klasa in uczniowie.items():
                    if klasa == klasy_wychowawcy:
                        print(uczen)
            else:
                print("Nie ma takiego wychowawcy!")
        elif opcja == "5":
            break
        else:
            print("Zła komenda")


# główne menu
while True:
    print("\nWitamy w programie do zarządzania bazą szkolną \n")
    wybor = input(
        """Wybierz polecenie:
         1 - Utwórz użytkownika 
         2 - Zarządzaj użytkownikami
         3 - Koniec 
         Komenda: """
    )
    if wybor == "1":
        polecenie = input(
            """Wybierz jakiego rodzaju użytkownika chcesz utworzyć:
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
