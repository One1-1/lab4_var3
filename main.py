"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab4.my_library import task4_1, task4_2, task4_3, task4_4, task4_5, task4_6, task4_7



def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:

                print("Введите координаты трех вершин треугольника:")
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                x3 = float(input("x3: "))
                y3 = float(input("y3: "))


                area, perimeter = task4_1(x1, x2, x3, y1, y2, y3)

                print("Используя оператор %:")
                print("Площадь: %.2f, Периметр: %.2f" % (area, perimeter))

                print("Используя метод format():")
                print("Площадь: {:.2f}, Периметр: {:.2f}".format(area, perimeter))

                print("Используя f-строки:")
                print(f"Площадь: {area:.2f}, Периметр: {perimeter:.2f}")

            case 2:
                x = float(input("add num format - 0.00: "))
                task4_2(x)

            case 3:
                x = float(input("Введите x: "))

                print(task4_3(x))

            case 4:
                sum_amount = float(input("Введите сумму покупки: "))
                card_type = input("Введите тип дисконтной карты (s, m, l, e): ")
                task4_4(sum_amount, card_type)

            case 5:
                task4_5()

            case 6:

                current = int(input("Введите целое число (0 для завершения): "))
                print("Количество чисел, больших своих соседей:", task4_6(current))

            case 7:
                n = int(input("Введите число: "))
                first_5_hamming = task4_7(n)
                print(first_5_hamming)

                hamming_sum = sum(first_5_hamming)
                print(hamming_sum)

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break


