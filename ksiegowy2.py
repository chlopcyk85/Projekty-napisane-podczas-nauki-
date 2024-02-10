import json

produkt = 0


def wczytaj_historia():
    try:
        with open("historia.txt", "r") as plik:  # otwarcie pliku w trybie do zapisu
            return json.loads(plik.read())
    except FileNotFoundError:
        with open("historia.txt", "a") as plik:
            return []


def wczytaj_stan_konta():
    try:
        with open("stan_konta.txt", "r") as plik:  # otwarcie pliku w trybie do zapisu
            return float(plik.read())
    except FileNotFoundError:
        with open("stan_konta.txt", "w") as plik:
            return 0


def wczytaj_magazyn():
    try:
        with open("stan_magazynu.txt", "r") as plik:
            return json.loads(plik.read())

    except FileNotFoundError:
        with open("stan_magazynu.txt", "w") as plik:
            return {}


def wczytaj_magazyn_ceny():
    try:
        with open("stan_magazynu_ceny.txt", "r") as plik:
            return json.loads(plik.read())

    except FileNotFoundError:
        with open("stan_magazynu_ceny.txt", "w") as plik:
            return {}


def zapisz_magazyn(stan_magazynu):
    with open("stan_magazynu.txt", "w") as plik:
        plik.write(json.dumps(stan_magazynu))


def zapisz_stan(stan_konta):
    with open("stan_konta.txt", "w") as plik:
        plik.write(str(stan_konta))


def zapisz_magazyn_ceny(stan_magazynu_ceny):
    with open("stan_magazynu_ceny.txt", "w") as plik:
        plik.write(json.dumps(stan_magazynu_ceny))


def zapisz_historia(historia):
    with open("historia.txt", "a") as plik:
        plik.write(json.dumps(historia))


def saldo():
    global stan_konta

    wybor_saldo = input(
        """Chcesz wypłacić czy do dokonać wpłaty na konto? 
            * Wpłata
            * Wypłata 
            Wybór: """
    )
    wybor_saldo.lower()
    if wybor_saldo == "wpłata":
        try:
            kwota = int(input("Podaj kwotę: "))
            stan_konta = stan_konta + kwota
            historia.append(f"Wpłata na konto na kwotę: {kwota}")
        except:
            print("Podaj poprawną wartość ! ")
    elif wybor_saldo == "wypłata":
        kwota = int(input("Podaj kwotę: "))
        if kwota > stan_konta:
            print("Brak wystarczających środków na koncie! ")
        else:
            stan_konta = stan_konta - kwota
            historia.append(f"Wypłata z konta na kwotę: {kwota}")
    else:
        print("Podaj poprawną wartość")

    # menu SPRZEDAŻ, sprzedaż produktu o ile jest w magazynie


def sprzedaz():
    global produkt
    global stan_konta
    if magazyn == {}:
        print("Nie ma nic w magazynie")
    else:
        for produkt in magazyn:
            print(f"Na stanie mamy: \n {produkt}")
            produkt = input("Który produkt chcesz sprzedać? ")
        if produkt in magazyn:
            ile_sztuk = int(input("Ile sztuk? "))
            cena = float(input("Jaka jest kwota za 1 szt. ? "))
            magazyn[produkt] -= ile_sztuk
            cena_sprzedazy = ile_sztuk * cena
            stan_konta += cena_sprzedazy
            historia.append(
                f"Sprzedaż: {produkt}, Sztuk: {ile_sztuk} za cenę: {cena} zł"
            )
        else:
            print("Nie takiego produktu")

    # menu ZAKUP, zakup produktu wraz z obciążeniem stanu konta


def zakup():
    global stan_konta
    global produkt
    produkt = input("Podaj nazwę produktu: ")
    cena_produktu = float(input("Podaj cenę produktu: "))
    ilosc = int(input("Podaj ilość zakupionego produktu: "))
    if produkt in magazyn:
        magazyn[produkt] += ilosc
    elif cena_produktu * ilosc > stan_konta:
        print("Zakup nie może być zrealizowany, za mało środków na koncie! ")
    else:
        stan_konta = stan_konta - (cena_produktu * ilosc)
        magazyn[produkt] = ilosc
        ceny[produkt] = cena_produktu
        historia.append(f"Zakup: {produkt}, Sztuk: {ilosc} za cenę: {cena_produktu} zł")


# menu STAN KONTA
def konto():
    print(f"Stan konta wynosi: {stan_konta} zł")


def lista():
    global produkt
    print("Stan magazynu: ")
    for produkt, ilosc in magazyn.items():
        print(
            f"{produkt}: {ilosc} szt. w magazynie, zakup: ({ceny[produkt]} zł / szt.)",
            end="\n",
        )

    # menu STAN MAGAZYNU


def w_magazyn():
    for produkt in magazyn:
        print(f"Na stanie mamy: \n {produkt}")
    produkt = input("Wybierz produkt, by sprawdzić jego aktualny stan: ")
    if produkt in magazyn:
        print(produkt, "ilość:", magazyn[produkt])
    else:
        print("Nie ma takiego produktu na stanie")


# menu PRZEGLĄD, wyświetla historię wszystkich działań
def przeglad():
    global historia
    try:
        od = input('Wprowadź zakres "od" ')
        do = input('Wprowadź zakres "do" ')

        if od == "":
            print(historia[0::])
        elif do == "":
            print(historia[::-1])
        else:
            od2 = int(od)
            do2 = int(do)
            od2 >= 0 or do2 >= len(historia)
            for i in range(od2, do2 + 1):
                print(historia[i])
    except:
        print(f"Zły zakres. Zakres jest do 0 do {len(historia)}")


stan_konta = wczytaj_stan_konta()
magazyn = wczytaj_magazyn()
ceny = wczytaj_magazyn_ceny()
historia = wczytaj_historia()

while True:
    print(
        "\nWybierz operację której chcesz dokonać, wprowadź komendę z listy poniżej : \n"
    )
    print(" * saldo * sprzedaż * zakup * konto * lista * magazyn * przegląd * koniec (zapisz) ")
    wybor = input("Komenda: ")
    wybor.lower()
    if wybor == "saldo":
        saldo()
    elif wybor == "sprzedaż":
        sprzedaz()
    elif wybor == "zakup":
        zakup()
    elif wybor == "konto":
        konto()
    elif wybor == "lista":
        lista()
    elif wybor == "magazyn":
        w_magazyn()
    elif wybor == "przegląd":
        przeglad()
    elif wybor == "koniec":
        print("Do widzenia")
        zapisz_stan(stan_konta)
        zapisz_magazyn(magazyn)
        zapisz_magazyn_ceny(ceny)
        zapisz_historia(historia)
        break
    else:
        print("Nie dokonałeś żadnego wyboru")
    zapisz_stan(stan_konta)
    zapisz_magazyn(magazyn)
    zapisz_magazyn_ceny(ceny)
