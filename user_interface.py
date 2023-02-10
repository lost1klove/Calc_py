from excep import *
from mod_calc import *
from logg import logging

type_dict = {"1": "rational", "2": "complex"}
operator = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^", "6": "sqrt"}


def menu():
    print("Привет от Калькулятора! :)!\n")
    while True:
        type_n = input("Работаем с:"
                         "\n1 - Рациональные числа"
                         "\n2 - Комплексные числа"
                         "\n3 - Выход\n")
        match type_n:
            case "1" | "2":
                menu_calc(type_n)
            case "3":
                logging.info("Выход.")
                print("Скоро увидимся! Пока :)")
                break
            case _:
                logging.warning("Выбран неверный пункт")
                print("Ваш выбор не распознан! Попробуйте снова")


def menu_calc(data_type):
    global operator
    logging.info(f"Запуск меню. С {type_dict[data_type]}.")
    num_one, num_two = 0, 0
    res = "q"
    sgn = "/"
    while True:
        operatns = input("Операции:"
                   "\n1 - сумма"
                   "\n2 - разность"
                   "\n3 - умножение"
                   "\n4 - деление"
                   "\n5 - степень"
                   "\n6 - квадрат"
                   "\n7 - назад\n")

        if operatns.isdigit() and int(operatns) in range(1, 6):
            if data_type == "1":
                num_one, num_two = check_in([input(f"Введите {i + 1} число: ") for i in range(2)], data_type)
            elif data_type == "2":
                num_one, num_two = [complex(*check_in([input(f"Введите {i + 1} действительную часть: "),
                                                    input(f"Введите {i + 1} мнимую часть: ")], data_type, i))
                                 for i in range(2)]
        match operatns:
            case "1":
                res = sum_data(num_one, num_two)
                logging.info(f"Sum: {num_one} + {num_two} = {res}")
            case "2":
                res = sub_data(num_one, num_two)
                logging.info(f"Sub: {num_one} - {num_two} = {res}")
            case "3":
                res = mul_data(num_one, num_two)
                logging.info(f"Mul: {num_one} * {num_two} = {res}")
            case "4":
                if data_type == "1":
                    num_two = check_zero_real(str(num_two))
                    sign = menu_divisions()
                    operator[operatns] = sign
                else:
                    num_two = check_zero_comp(num_one, num_two)
                    operator[operatns] = "/"
                if sign:
                    res = div_data(num_one, num_two)
                    logging.info(f"Div: {num_one} {sign} {num_two} = {res}")
            case "5":
                res = pow_data(num_one, num_two)
                logging.info(f"Pow: {num_one} ^ {num_two} = {res}")
            case "6":
                num_two = ""
                if data_type == "1":
                    num_one = check_in_one([input(f"Введите числоа: ")], data_type)
                else:
                    num_one = complex(*check_in_one([input(f"Введите действительную часть: "),
                                                   input(f"Введите мнимую часть: ")], data_type))
                res = pow_data(num_one)
                logging.info(f"Sqrt: {num_one} = {res}")
            case "7":
                logging.info('Меню назад')
                print()
                break
            case _:
                logging.warning(f"Выбран неверный пункт, главное меню")
                print("Ошибка. Попробуйте снова")
                continue
        if res != "q":
            print(f"Результат: {num_one} {operator[operatns]} {num_two} = {res}", end="\n\n")


def menu_divisions():
    logging.info(f"начало разделения")
    while True:
        operatns = input("Операции:\n"
                   "1 - '/'\n"  
                   "2 - '//'\n"
                   "3 - '%'\n"
                   "4 - назад\n")
        match operatns:
            case "1":
                return "/"
            case "2":
                return "//"
            case "3":
                return "%"
            case "4":
                logging.info('остановка разделения')
                print()
                return 0
            case _:
                logging.warning(f"Выбран неверный элемент. Главное меню")
                print("Ошибка! Попробуйте еще.")