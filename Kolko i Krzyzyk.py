# import potrzebnych bibliotek (generowanie losowych liczb)
import random

# zmienne
pole = [" - ", " - ", " - ", " - ", " X ", " - ", " - ", " - ", " - "]
wybor = 0

# powitanie
print("\nWitaj w grze Kółko i Krzyżyk :)\n")
print("Czy potrafisz wygrać z komputerowym przeciwnikiem? ")
print("Plansza składa się pól (1-9)")
print(
    """  1    2    3
  4    5    6
  7    8    9"""
)
print('Dla ułatwienia, "komputer" zaczyna jako pierwszy')


# rysowanie planszy
def plansza():
    print(pole[0] + " | " + pole[1] + " | " + pole[2])
    print("---------------")
    print(pole[3] + " | " + pole[4] + " | " + pole[5])
    print("---------------")
    print(pole[6] + " | " + pole[7] + " | " + pole[8])


# ruch gracza komputerowego
def ruch_pc():
    while True:
        if pole[0] == " - ":
            pole[0] = " X "
            break
        elif pole[2] == " - ":
            pole[2] = " X "
            break
        elif pole[6] == " - ":
            pole[6] = " X "
            break
        elif pole[8] == " - ":
            pole[8] = " X "
            break
        else:
            wybor_pc = random.randint(0, 8)
            if pole[wybor_pc] == " O ":
                continue
            elif pole[wybor_pc] == " X ":
                continue
            else:
                pole[wybor_pc] = " X "
                break


# sprawdzanie wyniku
def wynik():
    if pole[0] == " X " and pole[1] == " X " and pole[2] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif pole[3] == " X " and pole[4] == " X " and pole[5] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif pole[6] == " X " and pole[7] == " X " and pole[8] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif pole[0] == " X " and pole[3] == " X " and pole[6] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif pole[1] == " X " and pole[4] == " X " and pole[7] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif pole[2] == " X " and pole[5] == " X " and pole[8] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif pole[0] == " X " and pole[4] == " X " and pole[8] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif pole[2] == " X " and pole[4] == " X " and pole[6] == " X ":
        print("\nP R Z E G R A Ł E Ś !\n")
        return "stop"
    elif " - " not in pole:
        print("\nMamy REMIS !\n")
        return "stop"


# ruch gracza
def gracz():
    while True:
        try:
            wybor = int(input("Wybierz pole które TY chcesz zagrać: ")) - 1
            if wybor in range(0, 9):
                if pole[wybor] == " - ":
                    pole[wybor] = " O "
                    break
        except:
            print("Błąd, wybierz poprawnie!")
            continue


# główna pętla
while True:
    plansza()

    gracz()

    ruch_pc()

    if wynik() == "stop":
        plansza()
        break
