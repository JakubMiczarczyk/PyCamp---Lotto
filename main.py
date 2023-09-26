import random

numbers_pull = range(1, 50)
my_types = {2, 4, 34, 38, 41, 46}
game_time = 3 * 4 * 12


def draw():
    return set(random.sample(numbers_pull, k=6))


if __name__ == '__main__':
    draw_numbers = {}
    counter = 0

    while my_types != draw_numbers:
        draw_numbers = draw()
        counter += 1

    total_cost_of_draws = 3 * counter
    print(f'Liczba losowań do trafienia "6": {counter:,}')
    print(f'Trafienie "6" przy założeniu,'
          f'\nże gramy 3 razy w tygodniu zajełoby Ci {(counter / game_time):,.0} lat.'
          f'\na poniesiony koszt zakładów {total_cost_of_draws:,} zł')
