import random

numbers_pull = range(1, 50)
game_time = 2 * 4 * 12
n = 6


def draw():
    return set(random.sample(numbers_pull, k=6))


def lucky_numbers():
    numbers = set()
    # n = 6

    num_count = 0
    for i in range(0, n):
        number = int(input(f'Podaj swój szczęśliwy numer z zakersu:\n'
                           f'{numbers_pull}\n: '))
        if number not in numbers_pull:
            print('Podano zły numer.\n'
                  'Podaj numer z zakresu:\n'
                  f'{numbers_pull}')  # Popraw wyświetlanie
        else:
            numbers.add(number)
            num_count += 1
            print(f'Podano {num_count}/{n} numerów')
    return numbers


def game():
    draw_numbers = {}
    counter = 0

    print(f'Podaj {n} szczęsiwych numerów z zakresu {numbers_pull}')

    player_numbers = lucky_numbers()

    print('Obliczam kiedy Kiedy trafisz "6"...\n')

    while player_numbers != draw_numbers:
        draw_numbers = draw()
        counter += 1

    total_cost_of_draws = 4 * counter
    print(f'Liczba losowań do trafienia "6": {counter:,}')
    print(f'Trafienie "6" przy założeniu,'
          f'\nże gramy 3 razy w tygodniu zajełoby Ci {(counter / game_time):,.0} lat.'
          f'\na poniesiony koszt zakładów {total_cost_of_draws:,} zł')
