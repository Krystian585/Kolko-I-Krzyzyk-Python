def wyswietl_plansze(plansza):
    pustaplansza=""""
 ___________________
|   7  |   8  |  9  |
| ----------------- |
|   4  |   5  |  6  |
| ----------------- |
|   1  |   2  |  3  |
| ----------------- |
"""
    for i in range(1, 10):# zrobienie planszy - pusta lista
        if (plansza[i] == 'O' or plansza[i] == 'X'):
            pustaplansza = pustaplansza.replace(str(i), plansza[i])
        else:
            pustaplansza = pustaplansza.replace(str(i), ' ')
    print(pustaplansza)


def znak_uzytkownika():  #wybor przez uzytkownika x albo y
    uzytkownik1 = input("Wybierz 'X' albo 'O' ")
    while True:
        if uzytkownik1.upper() == 'X':  #sprawdza wielkosci tez
            uzytkownik2='O'
            print("Wybrales " + uzytkownik1 + ". uzytkownik 2 bedzie " + uzytkownik2)
            return uzytkownik1.upper(),uzytkownik2
        elif uzytkownik1.upper() == 'O':
            uzytkownik2='X'
            print("Wybrales " + uzytkownik1 + ". uzytkownik 2 bedzie " + uzytkownik2)
            return uzytkownik1.upper(),uzytkownik2
        else:
            uzytkownik1 = input("Wybierz 'X' albo 'O' ")


def przypisywanie_znaku(plansza, znak, pozycja):
    plansza[pozycja] = znak  # przypisywanie znaku do listy
    return plansza


def sprawdzanie_miejsca(plansza, pozycja):  #zwraca # jesli miejsce wolne
    return plansza[pozycja] == '#'


def wybor_uzytkownika(plansza):   #pytanie o wybor
    wybor = input("Wybierz miejsce pomiedzy 1 a 9 : ")
    while not sprawdzanie_miejsca(plansza, int(wybor)):
        wybor = input("Miejsce zajete. Wybierz inne pomiedzy 1 a 9 : ")
    return wybor


def czy_plansza_pelna(plansza):
    return len([x for x in plansza if x == '#']) == 1


def sprawdzanie_wygranej(plansza, znak):
    if plansza[1] == plansza[2] == plansza[3] == znak:  #poziomo
        return True
    if plansza[4] == plansza[5] == plansza[6] == znak:  #poziomo
        return True
    if plansza[7] == plansza[8] == plansza[9] == znak:  #poziomo
        return True
    if plansza[1] == plansza[4] == plansza[7] == znak:  #pionowo
        return True
    if plansza[2] == plansza[5] == plansza[8] == znak:  #pionowo
        return True
    if plansza[3] == plansza[6] == plansza[9] == znak:  #pionowo
        return True
    if plansza[1] == plansza[5] == plansza[9] == znak:  #przekatne
        return True
    if plansza[3] == plansza[5] == plansza[7] == znak:  #przekatne
        return True
    return False


def granie_ponownie():
    grajznowu = input("Chcesz zagrac ponownie? (t/n) ")
    if grajznowu.lower() == 't':
        return True
    if grajznowu.lower() == 'n':
        return False


if __name__ == "__main__":
    i = 1
    uzytkownicy=znak_uzytkownika()
    plansza = ['#'] * 10  #wypelnienei tablicy
    while True:
        start = czy_plansza_pelna(plansza)
        while not start:
            pozycja = wybor_uzytkownika(plansza) # wybor miejsca na wstawienie znaku
            # ktory uzytkownik i jaki znak
            if i % 2 == 0:
                znak = uzytkownicy[1]
            else:
                znak = uzytkownicy[0]
            przypisywanie_znaku(plansza, znak, int(pozycja)) #wpisywanie znaku do danego miejsca
            wyswietl_plansze(plansza)
            i += 1 #aby zmieniac gracza
            if sprawdzanie_wygranej(plansza, znak):
                print("Wygrales !")
                break
            start=czy_plansza_pelna(plansza)
        if not granie_ponownie():
            break
        else:
            i = 1
            uzytkownicy=znak_uzytkownika()
            board = ['#'] 
