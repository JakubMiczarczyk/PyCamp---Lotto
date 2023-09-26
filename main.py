import random

numbers_pull = range(1, 50)
game_time = 3 * 4 * 12


def draw():
    return set(random.sample(numbers_pull, k=6))


def lucky_numbers():
    numbers = set()
    n = 6
    for i in range(0, n):
        number = int(input())
        numbers.add(number)
    return numbers


if __name__ == '__main__':
    draw_numbers = {}
    counter = 0

    player_numbers = lucky_numbers()

    while player_numbers != draw_numbers:
        draw_numbers = draw()
        counter += 1

    total_cost_of_draws = 3 * counter
    print(f'Liczba losowań do trafienia "6": {counter:,}')
    print(f'Trafienie "6" przy założeniu,'
          f'\nże gramy 3 razy w tygodniu zajełoby Ci {(counter / game_time):,.0} lat.'
          f'\na poniesiony koszt zakładów {total_cost_of_draws:,} zł')
