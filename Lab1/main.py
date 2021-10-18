import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def print_pair_root(a):
    first_root = math.sqrt(a)
    second_root = - math.sqrt(a)
    print(first_root, second_root)


def print_zero():
    print(0)


def print_roots(roots):
    len_roots = len(roots)

    if len_roots == 0:
        print(roots + 'Нет корней')
        return

    if len_roots == 1:
        if roots[0] == 0:
            print_zero()
        else:
            print_pair_root(roots[0])
        return

    if len_roots == 2:
        if roots[0] == 0:
            print_zero()
            print_pair_root(roots[1])
            return
        if roots[1] == 0:
            print_zero()
            print_pair_root(roots[0])
            return

        print_pair_root(roots[0])
        print_pair_root(roots[1])


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)
    print_roots(roots)


if __name__ == "__main__":
    main()
