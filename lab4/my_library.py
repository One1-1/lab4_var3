from turtledemo.penrose import start


def task4_1(a, b, c):
    '''
    Вычислите дробную часть среднего геометрического трёх заданных
    вещественных чисел

    :param a: вводимое число
    :param b: вводимое число
    :param c: вводимое число
    :return drob_part: дробная часть среднего геометрического
    '''

    # Вычисление среднего геометрического
    geometric_mean = (a * b * c) ** (1 / 3)

    # Вычисление дробной части
    drob_part = geometric_mean - int(geometric_mean)

    # Вывод дробной части
    return drob_part

def task4_2(x):
    '''
    Второй младший разряд (десятки) целой части числа х больше 3, но не
    больше 7 и больше второго разряда дробной части

    :param x: вводимое число
    :return: None
    '''

    # Получаем целую и дробную части числа
    integer_part = int(x)
    fractional_part = x - integer_part

    # Получаем второй младший разряд целой части (десятки)
    tens_digit = (integer_part // 10) % 10

    # Получаем второй разряд дробной части
    drob_str = str(fractional_part)[2:]  # Преобразуем дробную часть в строку и убираем "0."
    second_fractional_digit = int(drob_str[1]) if len(drob_str) > 1 else -1

    # условие
    if 3 < tens_digit <= 7 and tens_digit > second_fractional_digit:
        print("Условия выполнены.")
    else:
        print("Условия не выполнены.")


def task4_3(x):
    '''
    Составить программу для вычисления значений функции y = f(x) при
    произвольных значениях x. (a, b – константы)

    :param x: аргумент функции y = f(x)
    :return y: результат
    '''
    from math import sin, sqrt, log

    a = 0.19
    b = 6.1
    e = 2.71

    if x <= -1:
        y = e**(sin(x))
    if x > 5:
        y = log(abs(b*x))**2
    if -1 < x <= 5:
        y = sqrt(1 + (a*x)**2)

    return y



def task4_4(operation, start_cost):
    '''
    Разработать программу, которая определяет по типу операции с товаром его
    выходную стоимость: перемещение (p) - 0% накрутки от начальной стоимости;
    оптовая реализация (o) - 5% накрутки; розничная (r) - 15% накрутки,
    безналичная (b) - 7% накрутки. В программу вводится тип операции (один из
    символов: p, o, r, b) и начальная стоимость товара, на выходе - процент накрутки
    и итоговая стоимость.

    :param operation: тип операции
    :param start_cost: начальная стоимость
    :return: None
    '''

    percent = 0
    final_cost = start_cost

    match operation:
        case 'p':
            percent = 0
        case 'o':
            percent = 5
        case 'r':
            percent = 15
        case 'b':
            percent = 7
        case _:
            print("Некорректный тип операции.")
            exit()

    # итоговая стоимость
    final_cost += start_cost * (percent / 100)
    final_cost += start_cost * (percent / 100)

    print(f"Процент накрутки: {percent}%")
    print(f"Итоговая стоимость: {final_cost:.2f}")


def task4_5():
    '''
    Дана последовательность целых чисел, за которой следует ноль.
    Определить какой из элементов максимальный или минимальный
    встречается в ней раньше.

    :return: максмальное или минимальное значение
    '''
    max_num = None
    min_num = None
    max_index = -1
    min_index = -1
    index = 0

    while True:
        num = int(input())
        if num == 0:
            break
        if max_num is None or num > max_num:
            max_num = num
            max_index = index
        if min_num is None or num < min_num:
            min_num = num
            min_index = index
        index += 1

    if max_index < min_index:
        return max_num
    else:
        return min_num


def task4_6():
    '''
    Определить количество трехзначных чисел, сумма цифр которых простое число.

    :return count: кол-во трехзначных чисел
    '''
    count = 0

    for number in range(100, 1000):

        # Выделяем цифры числа
        hundreds = number // 100
        tens = (number // 10) % 10
        units = number % 10

        # Считаем сумму цифр
        digits_sum = hundreds + tens + units

        # Проверка, является ли сумма простым числом
        if digits_sum > 1:
            flag = True
            for i in range(2, int(digits_sum ** 0.5) + 1):
                if digits_sum % i == 0:
                    flag = False
                    break
            if flag:
                count += 1

    return count

def task4_7(n):

    for i in range(1, n + 1):
        str_i = str(i)
        flag = True
        # Перебираем каждую цифру
        for digit in str_i:
            # Если цифра равна '0' или число не делится на эту цифру, устанавливаем флаг в False
            if digit == '0' or i % int(digit) != 0:
                flag = False
                break
        if flag:
            return i




