from main import lucky_numbers
import random


def test_draw():
    # given
    numbers_pull = range(1, 50)
    # when
    draw_set = random.sample(numbers_pull, k=6)
    # then
    assert len(set(draw_set)) == 6


def test_lucky_numbers():   # TODO
    given_numbers = {1, 2, 3, 4, 5, 6}
    lucky_numbers()
    assert given_numbers == lucky_numbers()
