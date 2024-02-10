import json

class Sklep:
    def __init__(self):
        self.produkt = 0
        self.stan_konta = self.wczytaj_stan_konta()
        self.magazyn = self.wczytaj_magazyn()
        self.ceny = self.wczytaj_magazyn_ceny()
        self.historia = self.wczytaj_historia()

    def wczytaj_historia(self):
        try:
            with open("historia.txt", "r") as plik:
                return [json.loads(line) for line in plik.readlines()]
        except FileNotFoundError:
            with open("historia.txt", "a") as plik:
                return []

    def wczytaj_stan_konta(self):
        try:
            with open("stan_konta.txt", "r") as plik:
                content = plik.read()
                return float(content) if content else 0
        except FileNotFoundError:
            with open("stan_konta.txt", "w") as plik:
                return 0

    def wczytaj_magazyn(self):
        try:
            with open("stan_magazynu.txt", "r") as plik:
                return json.loads(plik.read())
        except FileNotFoundError:
            with open("stan_magazynu.txt", "w") as plik:
                return {}

    def wczytaj_magazyn_ceny(self):
        try:
            with open("stan_magazynu_ceny.txt", "r") as plik:
                return json.loads(plik.read())
        except FileNotFoundError:
            with open("stan_magazynu_ceny.txt", "w") as plik:
                return {}

    def zapisz_magazyn(self):
        with open("stan_magazynu.txt", "w") as plik:
            plik.write(json.dumps(self.magazyn))

    def zapisz_stan(self):
        with open("stan_konta.txt", "w") as plik:
            plik.write(str(self.stan_konta))

    def zapisz_magazyn_ceny(self):
        with open("stan_magazynu_ceny.txt", "w") as plik:
            plik.write(json.dumps(self.ceny))

    def zapisz_historia(self):
        with open("historia.txt", "a") as plik:
            for entry in self.historia:
                plik.write(json.dumps(entry) + '\n')

    def saldo(self):
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
                self.stan_konta = self.stan_konta + kwota
                self.historia.append(f"Wpłata na konto na kwotę: {kwota}")
            except:
                print("Podaj poprawną wartość ! ")
        elif wybor_saldo == "wypłata":
            kwota = int(input("Podaj kwotę: "))
            if kwota > self.stan_konta:
                print("Brak wystarczających środków na koncie! ")
            else:
                self.stan_konta = self.stan_konta - kwota
                self.historia.append(f"Wypłata z konta na kwotę: {kwota}")
        else:
            print("Podaj poprawną wartość")

    def sprzedaz(self):
        if not self.magazyn:
            print("Nie ma nic w magazynie")
        else:
            for produkt in self.magazyn:
                print(f"Na stanie mamy: \n {produkt}")
                produkt = input("Który produkt chcesz sprzedać? ")
            if produkt in self.magazyn:
                ile_sztuk = int(input("Ile sztuk? "))
                cena = float(input("Jaka jest kwota za 1 szt. ? "))
                self.magazyn[produkt] -= ile_sztuk
                cena_sprzedazy = ile_sztuk * cena
                self.stan_konta += cena_sprzedazy
                self.historia.append(
                    f"Sprzedaż: {produkt}, Sztuk: {ile_sztuk} za cenę: {cena} zł"
                )
            else:
                print("Nie takiego produktu")

    def zakup(self):
        produkt = input("Podaj nazwę produktu: ")
        cena_produktu = float(input("Podaj cenę produktu: "))
        ilosc = int(input("Podaj ilość zakupionego produktu: "))
        if produkt in self.magazyn:
            self.magazyn[produkt] += ilosc
        elif cena_produktu * ilosc > self.stan_konta:
            print("Zakup nie może być zrealizowany, za mało środków na koncie! ")
        else:
            self.stan_konta -= cena_produktu * ilosc
            self.magazyn[produkt] = ilosc
            self.ceny[produkt] = cena_produktu
            self.historia.append(
                f"Zakup: {produkt}, Sztuk: {ilosc} za cenę: {cena_produktu} zł"
            )

    def konto(self):
        print(f"Stan konta wynosi: {self.stan_konta} zł")

    def lista(self):
        print("Stan magazynu: ")
        for produkt, ilosc in self.magazyn.items():
            print(
                f"{produkt}: {ilosc} szt. w magazynie, zakup: ({self.ceny[produkt]} zł / szt.)",
                end="\n",
            )

    def w_magazyn(self):
        for produkt in self.magazyn:
            print(f"Na stanie mamy: \n {produkt}")
        produkt = input("Wybierz produkt, by sprawdzić jego aktualny stan: ")
        if produkt in self.magazyn:
            print(produkt, "ilość:", self.magazyn[produkt])
        else:
            print("Nie ma takiego produktu na stanie")

    def przeglad(self):
        try:
            od = input('Wprowadź zakres "od" ')
            do = input('Wprowadź zakres "do" ')

            if od == "":
                print(self.historia[0::])
            elif do == "":
                print(self.historia[::-1])
            else:
                od2 = int(od)
                do2 = int(do)
                od2 >= 0 or do2 >= len(self.historia)
                for i in range(od2, do2 + 1):
                    print(self.historia[i])
        except:
            print(f"Zły zakres. Zakres jest od 0 do {len(self.historia)}")

    def uruchom_sklep(self):
        while True:
            print(
                "\nWybierz operację której chcesz dokonać, wprowadź komendę z listy poniżej : \n"
            )
            print(
                " * saldo * sprzedaż * zakup * konto * lista * magazyn * przegląd * koniec (zapisz) "
            )
            wybor = input("Komenda: ")
            wybor.lower()
            if wybor == "saldo":
                self.saldo()
            elif wybor == "sprzedaż":
                self.sprzedaz()
            elif wybor == "zakup":
                self.zakup()
            elif wybor == "konto":
                self.konto()
            elif wybor == "lista":
                self.lista()
            elif wybor == "magazyn":
                self.w_magazyn()
            elif wybor == "przegląd":
                self.przeglad()
            elif wybor == "koniec":
                print("Do widzenia")
                self.zapisz_stan()
                self.zapisz_magazyn()
                self.zapisz_magazyn_ceny()
                self.zapisz_historia()
                break
            else:
                print("Nie dokonałeś żadnego wyboru")
            self.zapisz_stan()
            self.zapisz_magazyn()
            self.zapisz_magazyn_ceny()


if __name__ == "__main__":
    sklep = Sklep()
    sklep.uruchom_sklep()
