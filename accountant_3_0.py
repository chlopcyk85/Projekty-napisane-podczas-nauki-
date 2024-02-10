import json
import sys


class Manager:
    def __init__(self):
        self.stan_konta = self.wczytaj_stan_konta()
        self.magazyn = self.wczytaj_magazyn()
        self.ceny = self.wczytaj_magazyn_ceny()
        self.historia = self.wczytaj_historia()
        self.actions = {}
        self.assign_decorators()

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Została podana zła komenda")
        else:
            self.actions[name](self)

    def assign_decorators(self):
        @self.assign("saldo")
        def saldo(self):
            wybor_saldo = input(
                """Chcesz wypłacić czy dokonać wpłaty na konto? 
                    * Wpłata
                    * Wypłata 
                    Wybór: """
            ).lower()

            if wybor_saldo == "wpłata":
                try:
                    kwota = int(input("Podaj kwotę: "))
                    self.stan_konta += kwota
                    self.historia.append(f"Wpłata na konto na kwotę: {kwota}")
                except ValueError:
                    print("Podaj poprawną wartość ! ")
            elif wybor_saldo == "wypłata":
                kwota = int(input("Podaj kwotę: "))
                if kwota > self.stan_konta:
                    print("Brak wystarczających środków na koncie! ")
                else:
                    self.stan_konta -= kwota
                    self.historia.append(f"Wypłata z konta na kwotę: {kwota}")
            else:
                print("Podaj poprawną wartość")

        @self.assign("sprzedaż")
        def sprzedaz(self):
            if not self.magazyn:
                print("Nie ma nic w magazynie")
            else:
                [print(f"Na stanie mamy: \n {produkt}") for produkt in self.magazyn]
                produkt_sprzedaz = input("Który produkt chcesz sprzedać? ")
                if produkt_sprzedaz in self.magazyn:
                    ile_sztuk = int(input("Ile sztuk? "))
                    cena = float(input("Jaka jest kwota za 1 szt. ? "))
                    self.magazyn[produkt_sprzedaz] -= ile_sztuk
                    cena_sprzedazy = ile_sztuk * cena
                    self.stan_konta += cena_sprzedazy
                    self.historia.append(
                        f"Sprzedaż: {produkt_sprzedaz}, Sztuk: {ile_sztuk} za cenę: {cena} zł"
                    )
                else:
                    print("Nie ma takiego produktu")

        @self.assign("zakup")
        def zakup(self):
            produkt_zakup = input("Podaj nazwę produktu: ")
            cena_produktu = float(input("Podaj cenę produktu: "))
            ilosc = int(input("Podaj ilość zakupionego produktu: "))
            if produkt_zakup in self.magazyn:
                self.magazyn[produkt_zakup] += ilosc
            elif cena_produktu * ilosc > self.stan_konta:
                print("Zakup nie może być zrealizowany, za mało środków na koncie! ")
            else:
                self.stan_konta -= cena_produktu * ilosc
                self.magazyn[produkt_zakup] = ilosc
                self.ceny[produkt_zakup] = cena_produktu
                self.historia.append(
                    f"Zakup: {produkt_zakup}, Sztuk: {ilosc} za cenę: {cena_produktu} zł"
                )

        @self.assign("konto")
        def konto(self):
            print(f"Stan konta wynosi: {self.stan_konta} zł")

        @self.assign("lista")
        def lista(self):
            print("Stan magazynu: ")
            [
                print(
                    f"{produkt}: {ilosc} szt. w magazynie, zakup: ({self.ceny[produkt]} zł / szt.)",
                    end="\n",
                )
                for produkt, ilosc in self.magazyn.items()
            ]

        @self.assign("magazyn")
        def w_magazyn(self):
            [print(f"Na stanie mamy: \n {produkt}") for produkt in self.magazyn]
            produkt_w_magazyn = input("Wybierz produkt, by sprawdzić jego aktualny stan: ")
            if produkt_w_magazyn in self.magazyn:
                print(produkt_w_magazyn, "ilość:", self.magazyn[produkt_w_magazyn])
            else:
                print("Nie ma takiego produktu na stanie")

        @self.assign("przegląd")
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
                    [print(self.historia[i]) for i in range(od2, do2 + 1)]
            except ValueError:
                print(f"Zły zakres. Zakres jest od 0 do {len(self.historia)}")

        @self.assign("koniec")
        def koniec(self):
            print("Do widzenia")
            self.zapisz_stan()
            self.zapisz_magazyn()
            self.zapisz_magazyn_ceny()
            self.zapisz_historia()
            sys.exit()
    def wczytaj_historia(self):
        try:
            with open("historia.txt", "r") as plik:
                return json.loads(plik.read())
        except FileNotFoundError:
            with open("historia.txt", "a") as plik:
                return []

    def wczytaj_stan_konta(self):
        try:
            with open("stan_konta.txt", "r") as plik:
                return float(plik.read())
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
            plik.write(json.dumps(self.historia))

    def run(self):
        while True:
            print(
                "\nWybierz operację, której chcesz dokonać. Wprowadź komendę z listy poniżej: \n"
            )
            print(
                " * saldo * sprzedaż * zakup * konto * lista * magazyn * przegląd * koniec (zapisz) "
            )
            wybor = input("Komenda: ").lower()

            self.execute(wybor)


if __name__ == "__main__":
    manager = Manager()
    manager.run()
