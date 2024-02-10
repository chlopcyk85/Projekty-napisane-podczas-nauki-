stan_konta = 0
magazyn = {}
historia = []
ceny= {}
produkt=0
while True:

    # wyświetlanie menu do którego program będzie wracał
    print("\nWybierz operację której chcesz dokonać, wprowadź komendę z listy poniżej : \n")
    print(" * saldo * sprzedaż * zakup * konto * lista * magazyn * przegląd * koniec")
    wybor = input("Komenda: ")
    wybor.lower()

    # menu SALDO, możliwość wpłaty oraz wypłaty z konta
    if wybor == "saldo":
        wybor_saldo = input("""Chcesz wypłacić czy do dokonać wpłaty na konto? 
            * Wpłata
            * Wypłata 
            Wybór: """)
        wybor_saldo.lower()
        if wybor_saldo == "wpłata":
            try:
                kwota = float(input("Podaj kwotę: "))
                stan_konta = stan_konta + kwota
                historia.append(f"Wpłata na konto na kwotę: {kwota}")
            except:
                print("Podaj poprawną wartość ! ")
        elif wybor_saldo == "wypłata":
            kwota = float(input("Podaj kwotę: "))
            if kwota > stan_konta:
                print("Brak wystarczających środków na koncie! ")
            else:
                stan_konta = stan_konta - kwota
                historia.append(f"Wypłata na konto na kwotę: {kwota}")
        else:
            print("Podaj poprawną wartość")

    # menu SPRZEDAŻ, sprzedaż produktu o ile jest w magazynie
    elif wybor == "sprzedaż":
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
            historia.append(f"Sprzedaż: {produkt}, Sztuk: {ile_sztuk} za cenę: {cena} zł")
        else:
            print("Nie takiego produktu")

    # menu ZAKUP, zakup produktu wraz z obciążeniem stanu konta
    elif wybor == "zakup":
        produkt = input("Podaj nazwę produktu: ")
        cena_produktu = float(input("Podaj cenę produktu: "))
        ilosc = int(input("Podaj ilość zakupionego produktu: "))
        if  produkt in magazyn:
            magazyn[produkt] += ilosc
        elif cena_produktu * ilosc > stan_konta:
            print("Zakup nie może być zrealizowany, za mało środków na koncie! ")
        else:
            stan_konta = stan_konta - (cena_produktu * ilosc)
            magazyn[produkt] = ilosc
            ceny[produkt] = cena_produktu
            historia.append(f"Zakup: {produkt}, Sztuk: {ilosc} za cenę: {cena_produktu} zł")

    # menu STAN KONTA
    elif wybor == "konto":
        print(f"Stan konta wynosi: {stan_konta} zł")

    # menu LISTA wraz ze szczegółami takimi jak ilość oraz cena zakupu
    elif wybor == "lista":
        print("Stan magazynu: ")
        for produkt, ilosc in magazyn.items():
                print(f'{produkt}: {ilosc} szt. w magazynie, zakup: ({ceny[produkt]} zł / szt.)', end='\n')

    # menu STAN MAGAZYNU
    elif wybor == "magazyn":
        for produkt in magazyn:
            print(f"Na stanie mamy: \n {produkt}")
        produkt = input("Wybierz produkt, by sprawdzić jego aktualny stan: ")
        if produkt in magazyn:
                print(produkt, "ilość:", magazyn[produkt])
        else:
            print("Nie ma takiego produktu na stanie")
    # menu PRZEGLĄD, wyświetla historię wszystkich działań
    elif wybor == "przegląd":
        try:
            od = input("Wprowadź zakres \"od\" ")
            do = input("Wprowadź zakres \"do\" ")

            if od == "":
                print(historia[0::])
            elif do == "":
                print(historia[::-1])
            else:
                od2=int(od)
                do2=int(do)
                od2 >= 0 or do2 >= len(historia)
                for i in range(od2, do2+1):
                    print(historia[i])
        except:
                print(f"Zły zakres. Zakres jest do 0 do {len(historia)}")

    # KOŃCZYMY PROGRAM
    elif wybor == "koniec":
        print("Do widzenia")

    # powrót do menu gdy brak akcji
    else:
        print("Nie dokonałeś żadnego wyboru")
