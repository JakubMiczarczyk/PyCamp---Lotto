from random import Random, sample

print('Zagrajmy w LOTTO!\n\n'
      'Wybierz 6 liczb z przedziau od 1 do 49.\n'
      'Zakład kosztuje 3 zł, ciekawe ile wydasz aby wygrać?')

wright_numbers = set(range(1, 50))

players_type = True

player_numbers = set()

# draw_set = set()


def player_input(number):
    player_numbers.add(number)


def check_numbers(numbers):
    if numbers.issubset(wright_numbers):
        print('\nPodano dobre liczby.\n'
              f'{player_numbers}\n'
              'Sprawdźmy je!')
    else:
        print('\nPodano złe liczby.\n'
              f'{player_numbers}\n'
              'Podaj 6 liczb od 1 do 49 Głąbie!\n')
    return bool


def draw():
    draw_set = set(sample([wright_numbers], k=6))  # TODO
    return draw_set


print('\nPoniżej podaj typowane liczby: ')

while players_type is True:
    if len(player_numbers) < 6:
        player_input(int(input('\nTypowana liczba: ')))
        players_type = True
    else:
        players_type = check_numbers(player_numbers)

print(f'Losowanie: {draw()}')
