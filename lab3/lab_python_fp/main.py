from time import sleep

from lab3.lab_python_fp.cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from unique import Unique


def test_field():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    field(goods, 'title', 'price')


def test_gen_random():
    print(gen_random(5, 1, 4))

def test_uniq():
    uniq = Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
    print([x for x in uniq])

    uniq = Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case=True)
    print([x for x in uniq])

    uniq = Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'])
    print([x for x in uniq])


def test_timer():
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_1():
        sleep(3.6)


def main():
    print("Задание 1:")
    test_field()
    print("Задание 2:")
    test_gen_random()
    print("Задание 3:")
    test_uniq()
    print("Задание 6:")
    test_timer()


if __name__ == "__main__":
    main()
