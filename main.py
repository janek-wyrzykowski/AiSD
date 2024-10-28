import networkx as nx
import random
import numpy


def graphgeneration(ulice):
    g = nx.Graph()



def main():
    print("Projekt 17: kurier \n")
    print("Wybierz metodę wrzucenia danych: \n")
    print("1. Dane wpisywane ręcznie, \n"
          "2. Dane losowe. \n")
    print("Wpisz swój wybór:\n")
    while True:
        wybor = input("")
        if wybor not in ['1', '2']:
            print("Nieprawidłowy wybór. Wpisz 1 lub 2.")
        else:
            break

    if wybor == '2':
        liczba_skrzyzowan = random.randint(1,100)
        n = ((liczba_skrzyzowan-1)*(liczba_skrzyzowan))/2
        if n > 300:
            n = 300

        liczba_ulic = random.randint(liczba_skrzyzowan, n)
        ulice = [[0 for i in range(liczba_skrzyzowan)] for i in range(liczba_skrzyzowan)]

        for i in range(2):
            for j in range(liczba_skrzyzowan):
                y = random.randint(1, liczba_skrzyzowan-1)
                while y == j or ulice[j][y] != 0:
                    y = random.randint(1, liczba_skrzyzowan-1)

                ulice[j][y] = random.randint(1, 100)
                ulice[y][j] = ulice[j][y]

        m = liczba_ulic - liczba_skrzyzowan
        if m > 0:
            for i in range(m-1):
                y = random.randint(1, liczba_skrzyzowan - 1)
                x = random.randint(1, liczba_skrzyzowan - 1)
                while y == x or ulice[x][y] != 0:
                    y = random.randint(1, liczba_skrzyzowan - 1)

                ulice[x][y] = random.randint(1, 100)
                ulice[y][x] = ulice[x][y]

        print(ulice)
        ulice = numpy.array(ulice)
        print(nx.from_numpy_array(ulice))

    else:
        print("Podaj liczbę skrzyżowań (1 <= n <= 100)")
        while True:
            liczba_skrzyzowan = int(input("")) + 1
            if liczba_skrzyzowan < 1 or liczba_skrzyzowan > 100:
                print("Nieprawidłowy wybór. Wpisz liczbę między 1 a 100.")
            else:
                break

        print("Podaj liczbę ulic (1 <= m <= 300)")
        while True:
            numer_ulic = int(input()) + 1
            if numer_ulic < 1 or numer_ulic > 300:
                print("Nieprawidłowy wybór. Wpisz liczbę między 1 a 300.")
            elif numer_ulic > (((liczba_skrzyzowan-1)*liczba_skrzyzowan)/2):
                print("Za dużo ulic na zadaną liczbę skrzyżowań!")
            elif numer_ulic < liczba_skrzyzowan:
                print("Za mało ulic na zadaną liczbę skrzyżowań!")
            else:
                break

        ulice = [[0 for i in range(liczba_skrzyzowan)] for i in range(liczba_skrzyzowan)]

        print("\n Przystąpimy do podawania ulic między skrzyżowaniami i czasu przejazdu tymi ulicami w miuntach.")
        print("\n Jeżeli czas przejazdu jest równy 0, to interpretujemy to jako brak połączenia między punktami.")
        print("\n Dane należy podawać w formacie 'a, b, c' , gdzie:")
        print("\n a - punkt a")
        print("\n b - punkt b")
        print("\n c - czas przejazdu")
        print("\n Jeżeli ulica istnieje już między dwoma punktami, to nie można jej nadpisać.")
        print("\n Przechodzimy do wpisywania:")

        for i in range(numer_ulic):
            podane = list(map(int, input("").strip().split(',')))[:numer_ulic]
            if podane[0] == podane[1] or ulice[podane[0]-1][podane[1]-1] != 0:
                while podane[0] == podane[1] or ulice[podane[0]-1][podane[1]-1] != 0:
                    print("Niepoprawna ulica. Ponów wpisanie danych")
                    podane = list(map(int, input("").strip().split(',')))[:numer_ulic]

            ulice[podane[0]-1][podane[1]-1] = podane[2]
            ulice[podane[1] - 1][podane[0] - 1] = podane[2]

        print(ulice)

if __name__ == "__main__":
    main()