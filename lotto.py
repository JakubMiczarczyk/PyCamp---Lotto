from random import Random

print('Zagrajmy w LOTTO!\n\n'
      'Wybierz 6 liczb z przedziau od 1 do 49.\n'
      'Zakład kosztuje 3 zł, ciekawe ile wydasz aby wygrać?')

wright_numbers = {1: 49}

players_type = True

player_numbers = set()


def player_input(number):
    player_numbers.add(number)


while players_type is True:
    print('\nPodaj typowane liczby: ')

    player_input(int(input('\nliczba 1 z 6: ')))
    player_input(int(input('liczba 2 z 6: ')))
    player_input(int(input('liczba 3 z 6: ')))
    player_input(int(input('liczba 4 z 6: ')))
    player_input(int(input('liczba 5 z 6: ')))
    player_input(int(input('liczba 6 z 6: ')))

    if player_numbers.issuperset(wright_numbers):
        players_type = False
        print('\nPodano dobre liczby.\n'
              'Sprawdźmy je!')
    else:
        players_type = True
        print('\nPodano złe liczby.\n'
              'Podaj 6 liczb od 1 do 49 Głąbie!\n')
