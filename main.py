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
        #tu wywolujemy funkcje ktora
        print("ehe")
    else:
        print("miau")


if __name__ == "__main__":
    main()