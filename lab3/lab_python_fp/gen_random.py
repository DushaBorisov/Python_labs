from random import randint


def gen_random(num_count, begin, end):
    return [randint(begin, end) for x in range(num_count)]
