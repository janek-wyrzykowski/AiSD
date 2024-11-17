import networkx as nx
import random
import numpy

def graph_generation():
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

    # dane losowe:
    if wybor == '2':
        liczba_skrzyzowan = random.randint(3, 100)
        n = ((liczba_skrzyzowan - 1) * (liczba_skrzyzowan)) / 2
        if n > 300:
            n = 300

        liczba_ulic = random.randint(liczba_skrzyzowan, n)
        ulice = [[0 for i in range(liczba_skrzyzowan)] for i in range(liczba_skrzyzowan)]

        for i in range(2):
            for j in range(liczba_skrzyzowan):
                niepuste = sum(x != 0 for x in ulice[j])
                if niepuste >= 2:
                    continue
                y = random.randint(0, liczba_skrzyzowan - 1)
                while y == j or ulice[j][y] != 0:
                    y = random.randint(0, liczba_skrzyzowan - 1)

                ulice[j][y] = random.randint(1, 100)
                ulice[y][j] = ulice[j][y]

        m = liczba_ulic - liczba_skrzyzowan
        if m > 0:
            for _ in range(m):
                y = random.randint(0, liczba_skrzyzowan - 1)
                x = random.randint(0, liczba_skrzyzowan - 1)
                while y == x or ulice[x][y] != 0:
                    y = random.randint(0, liczba_skrzyzowan - 1)
                    x = random.randint(0, liczba_skrzyzowan - 1)

                ulice[x][y] = random.randint(1, 100)
                ulice[y][x] = ulice[x][y]

        to_visit = dict()
        to_visit_amt = random.randint(1, min(19, liczba_skrzyzowan - 1))
        to_visit_list = random.sample(range(2, liczba_skrzyzowan + 1), to_visit_amt)
        to_visit = {i: int(i in to_visit_list) for i in range(2, liczba_skrzyzowan + 1)}
        to_visit.update({1: 1})


    # dane wpisane ręcznie
    else:
        print("Podaj liczbę skrzyżowań (1 <= n <= 100)")
        while True:
            liczba_skrzyzowan = int(input(""))
            if liczba_skrzyzowan < 1 or liczba_skrzyzowan > 100:
                print("Nieprawidłowy wybór. Wpisz liczbę między 1 a 100.")
            else:
                break

        print("Podaj liczbę ulic (1 <= m <= 300)")
        while True:
            numer_ulic = int(input())
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

        for _ in range(numer_ulic):
            podane = list(map(int, input("").strip().split(',')))[:numer_ulic]
            if podane[0] == podane[1] or ulice[podane[0]-1][podane[1]-1] != 0:
                while podane[0] == podane[1] or ulice[podane[0]-1][podane[1]-1] != 0:
                    print("Niepoprawna ulica. Ponów wpisanie danych")
                    podane = list(map(int, input("").strip().split(',')))[:numer_ulic]

            ulice[podane[0]-1][podane[1]-1] = podane[2]
            ulice[podane[1]-1][podane[0]-1] = podane[2]

        print('Przechodzimy do wybrania skrzyżowań do których musi dojechać kurier.')
        print('Proszę najpierw podać liczbę skrzyżowań, które musi odwiedzić dostawca:')
        liczba_do_odwiedzenia = int(input(''))
        while  0 >= liczba_do_odwiedzenia or liczba_do_odwiedzenia >= 20 or liczba_do_odwiedzenia > liczba_skrzyzowan:
            print('Niepoprawna liczba skrzyżowań do odwiedzenia. Wpisz liczbę ponownie.')
            liczba_do_odwiedzenia = int(input(''))

        print("Teraz nastąpi podawanie skrzyżowań. Skrzyżowania należy podawać w formacie 'a,b,c,d,...' ")
        print("NIE MOŻNA wybierać skrzyżowania 1, ponieważ to jest adres bazy.")
        odwiedzane = list(map(int, input("").strip().split(',')))[:numer_ulic]
        if len(odwiedzane) != liczba_do_odwiedzenia or min(odwiedzane) <= 1 or max(odwiedzane) > liczba_skrzyzowan \
                or odwiedzane[0] == 0:
                raise Exception('błędne dane. Koniec.')

        to_visit = {i: 0 for i in range(1, liczba_skrzyzowan+1)}
        for i in range(1, liczba_skrzyzowan+1):
            if i in odwiedzane:
                to_visit[i] = 1
        to_visit[1] = 1

    ulice = numpy.array(ulice)
    ulice = nx.from_numpy_array(ulice, nodelist=range(1, liczba_skrzyzowan+1))
    nx.set_node_attributes(ulice, to_visit, 'toVisit')
    return ulice