waga_suma = 0
paczki = 0
aktualna_waga = 0
waga_min = 20
paczka_min = 0

ilosc_paczek = int(input("Ile elementów chcesz wysłać? "))
if ilosc_paczek < 1:
    paczki -= 1
    print("Paczek musi być conajmniej 1 szt.")

for i in range(ilosc_paczek):
    while True:
        waga = int(input("Podaj wagę każdego elementu do wysłania: "))
        if waga < 1 or waga > 10:
            print("Waga paczki nieprawidłowa, elementy mogą ważyć od 1 kg do max 10 kg \n")
            print("Dodawanie paczek zostaje przerwane, a wszystkie paczki zostały wysłane\n")
            break
        waga_suma += waga
        if aktualna_waga + waga <= 20:
            aktualna_waga += waga
            break
        else:
            print("Waga paczki przekroczona, paczka została wysłana \n")
            paczki += 1
            aktualna_waga = waga
            break

if aktualna_waga <= waga_min:
    waga_min = 20 - aktualna_waga
    paczka_min = paczki + 1

paczki += 1

print("\nZostało wysłanych:", paczki, "paczek")
print("W tym: ")
print("    * Łączna waga elementów wyniosła:", waga_suma, "kg")
print("    * Suma pustych kilogramów wyniosła:", (20 * paczki) - waga_suma)
print("    * Paczka z największą liczbą pustych kilogramów ma nr", paczka_min, "z ilością", waga_min, "kg")
