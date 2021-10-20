from entity.House import House
from entity.HouseStreet import HouseStreet
from entity.Street import Street


def main():
    # Улицы
    streets = [
        Street(1, "Бауманская"),
        Street(2, "Никольская"),
        Street(3, "Семеновская"),
        Street(4, "Даниловская"),
    ]

    # Дома
    houses = [
        House(1, 33, 5, 1),
        House(2, 21, 1, 2),
        House(3, 56, 12, 3),
        House(4, 77, 2, 4),
        House(5, 66, 8, 2),
        House(6, 69, 9, 4),
        House(7, 12, 5, 3),
        House(8, 11, 2, 1),
    ]

    house_street = [
        HouseStreet(1, 1),
        HouseStreet(2, 2),
        HouseStreet(3, 3),
        HouseStreet(3, 1),
        HouseStreet(4, 2),
        HouseStreet(4, 4),
        HouseStreet(2, 3),
        HouseStreet(1, 3),
    ]

    # Связь один ко многим(улица - дом)
    one_to_many = [(h.number, h.floor, s.name)
                   for s in streets
                   for h in houses
                   if h.street_id == s.id]

    # Объединяем streets - house_street
    many_to_many_temp = [(s.name, hs.street_id, hs.house_id)
                         for s in streets
                         for hs in house_street
                         if s.id == hs.street_id]

    # Соединение данных многие ко многим
    many_to_many = [(h.number, h.floor, s_name)
                    for s_name, str_id, h_id in many_to_many_temp
                    for h in houses
                    if h.id == h_id]

    print('Задание А1')
    # Вывести список всех домов, у которых этажность больше 3, и названия улиц на которых они расположены

    res_1 = list(filter(lambda i: i[1] > 3, one_to_many))
    print(res_1)

    print('Задание А2')
    # Вывести список улиц с минимальной этажностью дома на каждой улице, отсортированный по минимальной этажности

    res_2 = []
    for s in streets:
        # список домов улицы
        s_houses = list(filter(lambda i: i[2] == s.name, one_to_many))
        if len(s_houses) > 0:
            res_2.append(min(s_houses, key=lambda i: i[1]))

    # сортиировка по этажности
    res_2 = sorted(res_2, key=lambda i: i[1])
    print(res_2)

    print('Задание А3')
    # Вывести список всех связанных домов и улиц, отсортированный по домам(сортировка по этажности дома)
    res_3 = sorted(many_to_many, key=lambda i: i[1])
    print(res_3)

if __name__ == "__main__":
    main()
