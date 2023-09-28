"""This Code count your possibility to win random games."""
import random

numbers_pull = range(1, 50)
GAME_TIME = 2 * 4 * 12
Z = 6


def draw() -> set:
    """
    This Function drawing random diferent numbers from given numbers pull
    :return: set of six random numbers
    """
    return set(random.sample(numbers_pull, k=6))


def lucky_numbers() -> set:
    """
    Take numbers for user and check is it in predefine set
    if it's not function ask for another number
    :return: set of users numbers
    """
    numbers = set()
    n_len = int(6)

    num_count = 0
    for number in range(0, n_len):
        number = int(input(f'Podaj swój szczęśliwy numer z zakersu:\n'
                           f'{numbers_pull}\n: '))
        if number not in numbers_pull:
            print('\nPodano zły numer.\n'  # Zła liczba też się nalicza do n TODO
                  'Podaj numer z zakresu:\n'
                  f'{numbers_pull}')        # popraw wyświetlanie
        elif number in numbers:
            print('\nPodany numer jest już w Twojej puli\n'
                  f'Podaj inny numer z zakresu:\n'
                  f'{numbers_pull}\n')
        else:
            numbers.add(number)
            num_count += 1
            print(f'Podano {num_count}/{n_len} numerów\n')
    return numbers


def game():
    """
    Starts lucky_numbers func and check numbers of draws to win.
    :return: number of draws, total cost of draws, time in years to win
    """
    draw_numbers = {}
    counter = 0

    print(f'Podaj {Z} szczęsiwych numerów z zakresu {numbers_pull}\n')

    player_numbers = lucky_numbers()

    print('Obliczam kiedy Kiedy trafisz "6"...\n')

    while player_numbers != draw_numbers:
        draw_numbers = draw()
        counter += 1

    total_cost_of_draws = 4 * counter
    print(f'Liczba losowań do trafienia "6": {counter:,}')
    print(f'Trafienie "6" przy założeniu,'
          f'\nże gramy 3 razy w tygodniu zajełoby Ci {(counter / GAME_TIME):,.0} lat.'
          f'\na poniesiony koszt zakładów {total_cost_of_draws:,} zł')
