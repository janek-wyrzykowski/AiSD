import networkx as nx

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
        #tu wywolujemy funkcje ktora zrobi cos
        print("ehe")
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
        lista = []
        for i in range(numer_ulic):
            podane = list(map(int, input("").strip().split(',')))[:numer_ulic]
            if podane[0] == podane[1]:
                print("Niepoprawna ulica. Ponów wpisanie danych")
                i -= 1
                continue
            if ulice[podane[0]-1][podane[1]-1] != 0:
                print("Dana ulica już istnieje! Ponów wpisanie danych")
                i -= 1
                continue

            ulice[podane[0]-1][podane[1]-1] = podane[2]
            ulice[podane[1] - 1][podane[0] - 1] = podane[2]

        print(ulice)

if __name__ == "__main__":
    main()