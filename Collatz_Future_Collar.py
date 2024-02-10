print("Witaj w programie obliczający ciag liczb tak zwany problem Collatz. ")

while True:
    x = int(input("Podaj liczbę całkowitą w zakresie od 1 do 100: "))
    if x > 100 or x < 0:
                print("Podałeś/aś złą liczbę, podaj liczbę raz jeszcze! ")
    else:
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = x * 3 + 1
                print(x)
