import random


def test_draw():
    # given
    numbers_pull = range(1, 50)
    # when
    draw_set = random.sample(numbers_pull, k=6)
    # then
    assert len(set(draw_set)) == 6
