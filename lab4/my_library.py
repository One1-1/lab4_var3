import math

def task4_1(x1, y1, x2, y2, x3, y3):
    '''
    По координатам трёх вершин некоторого треугольника найдите его
    площадь и периметр

    :param x1: координата вершины треугольника
    :param y1: координата вершины треугольника
    :param x2: координата вершины треугольника
    :param y2: координата вершины треугольника
    :param x3: координата вершины треугольника
    :param y3: координата вершины треугольника
    :return: area, perimeter
    '''
    a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    c = math.sqrt((x1-x3)**2 + (y1-y3)**2)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    return area, perimeter


def task4_2(x):
    '''
    Число, образованное двумя старшими разрядами дробной части числа
    х  [10; 30) U (40; 70]

    :param x: вводимое число
    :return: None
    '''
    isSpecial = 10<=((x*100)%100//1)<30 or 40<((x*100)%100//1)<=70
    print(((x*100)%100//1), isSpecial)


def task4_3(x):
    '''
    Составить программу для вычисления значений функции y = f(x) при
    произвольных значениях x. (a, b – константы)

    :param x: аргумент функции
    :return: результат выполнения функции
    '''
    from math import log, sqrt, atan

    A = 4.8
    B = 0.51

    if x <= -2:
        y = log(abs(x) + sqrt(A * x**2 + 1))
    elif x > 5:
        y = atan(B/(x**2 + 1))
    else:
        y = sqrt(A**2 + x**2)

    return f"y = {y:+7f}"


def task4_4(sum_amount, card_type):
    '''
    Составить программу, которая определяет размер скидки на товар, в
    зависимости от типа дисконтной карты. Типы карт: smart(s) - 3%, medium (m) -
    7%, large (l) - 12%, extra (e) - 20%. В программу вводится сумма покупки и
    символ, обозначающий тип карты. На экран выводится размер скидки и
    итоговая сумма

    :param sum_amount: сумма
    :param card_type: тип дисконтной карты
    :return: None
    '''


    match card_type:
        case 's':
            discount = sum_amount * (3 / 100)
            total_with_discount = sum_amount - discount
            print(f"Сумма скидки: {discount}")
            print(f"Сумма со скидкой: {total_with_discount}")
        case 'm':
            discount = sum_amount * (7 / 100)
            total_with_discount = sum_amount - discount
            print(f"Сумма скидки: {discount}")
            print(f"Сумма со скидкой: {total_with_discount}")
        case 'l':
            discount = sum_amount * (12 / 100)
            total_with_discount = sum_amount - discount
            print(f"Сумма скидки: {discount}")
            print(f"Сумма со скидкой: {total_with_discount}")
        case 'e':
            discount = sum_amount * (20 / 100)
            total_with_discount = sum_amount - discount
            print(f"Сумма скидки: {discount}")
            print(f"Сумма со скидкой: {total_with_discount}")
        case _:
            print(f"{card_type} Без скидки!")
            print(f"Сумма: {sum_amount}")



def task4_5():
    '''
    Найти все двузначные числа, сумма делителей которых четное число

    :param: None
    :return: None
    '''
    for i in range(10, 100):
        degit = 0
        for j in range(1, i + 1):
            if i % j == 0:
                degit += j
        if degit % 2 == 0:
            print(i)

def task4_6(current):
    '''
    Дана последовательность целых чисел, 0 – конец последовательности.
    Определить, сколько чисел больше своих соседей, т.е. предыдущего и последующего

    :param current: вводимое число
    :return: count количество чисел больше своих соседей
    '''
    count = 0
    prev = None

    while current != 0:
        next_number = int(input("Введите следующее целое число (0 для завершения): "))
        if next_number == 0:
            break

        if prev is not None and current > prev and current > next_number:
            count += 1

        prev = current
        current = next_number
    return count


def task4_7(n):
    '''
    Последовательность Хэмминга образуют натуральные числа, не имеющие
    других простых делителей, кроме 2, 3 и 5. Найти сумму первых n
    элементов этой последовательности

    :param n: кол-во элементов последовательности
    :return: сумма первых элементов последовательности
    '''
    hamming_numbers = [1]
    i2 = i3 = i5 = 0

    while len(hamming_numbers) < n:
        next_number = min(2 * hamming_numbers[i2], 3 * hamming_numbers[i3], 5 * hamming_numbers[i5])
        hamming_numbers.append(next_number)

        if next_number == 2 * hamming_numbers[i2]:
            i2 += 1
        if next_number == 3 * hamming_numbers[i3]:
            i3 += 1
        if next_number == 5 * hamming_numbers[i5]:
            i5 += 1

    return hamming_numbers






