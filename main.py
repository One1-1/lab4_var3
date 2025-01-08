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
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                c = float(input("Введите третье число: "))

                print("Дробная часть среднего геометрического:", task4_1(a, b, c))

            case 2:
                x = float(input("Введите число: "))

                task4_2(x)

            case 3:
                x = float(input('Введите x: '))

                print(task4_3(x))

            case 4:
                operation = input("Введите тип операции (p, o, r, b): ").strip().lower()
                start_cost = float(input("Введите начальную стоимость товара: "))

                print(task4_4(operation, start_cost))

            case 5:
                print(task4_5())

            case 6:

                print(task4_6())

            case 7:
                n = int(input("Введите число n: "))

                print(task4_7(n))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break


