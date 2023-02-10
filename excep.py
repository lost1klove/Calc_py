from typing import Union

from logg import logging

def check_in(dt: list, cntr: str, real_im=0):
    while True:
        check = [float(i) if "." in i else int(i) for i in dt if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if len(check) == 2:
            return check
        else:
            logging.warning(f"Введены некорректные значения: '{dt[0]}', '{dt[1]}'!")
            print(f"\n{'*' * 30}\n{'Попробуйте снова!':^30}\n{'*' * 30}\n")
            match cntr:
                case "1":
                    dt = [input(f"Введите {i + 1} число: ") for i in range(2)]
                case "2":
                    match real_im:
                        case 0:
                            dt = [input(f"Введите 1-ю действительную часть : "), input(f"Введите 1-ю мнимую часть : ")]
                        case 1:
                            dt = [input(f"Введите 2-ю действительную часть : "), input(f"Введите 2-ю мнимую часть: ")]



def check_in_one(dt: list, count: str):
    while True:
        check = [float(i) if "." in i else int(i) for i in dt if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        match count:
            case "1":
                if len(check) == 1:
                    return check[0]
                print(f"\n{'*' * 30}\n{'Попробуйте еще раз!':^30}\n{'*' * 30}\n")
                logging.warning(f"Введены некорректные значения: '{dt[0]}'!")
                dt = [input(f"Введите число: ")]
            case "2":
                if len(check) == 2:
                    return check
                print(f"\n{'*' * 30}\n{'Try again!':^30}\n{'*' * 30}\n")
                logging.warning(f"Введены некорректные значения: '{dt[0]}', '{dt[1]}'!")
                dt = [input(f"Введите действительную часть: "), input(f"Введите мнимую часть: ")]


def check_zero_real(dt: str):
    while True:
        d = [float(i) if "." in i else int(i) for i in [dt] if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if not (d and d[0]):
            print(f"\n{'*' * 50}\n{'Вы пытаетесь делить на ноль! Попробуйте снова.':^50}\n{'*' * 50}\n")
            logging.warning(f"Введено некорректное значение: '{dt}'!")
            dt = input(f"Введите второе число: ")
        else:
            return d[0]


def check_zero_comp(frst_data: Union[int, float], scnd_data: Union[int, float]):
    while True:
        try:
            frst_data / scnd_data
        except ZeroDivisionError:
            print(f"\n{'*' * 50}\n{'Вы пытаетесь делить на ноль! Попробуйте снова.':^50}\n{'*' * 50}\n")
            logging.warning(f"Введено некорректное значение: '{scnd_data}'!")
            scnd_data = complex(*check_in([input(f"Введите 2-ю действительную часть: "), input(f"Введите 2-ю мнимую часть: ")], "2", 1))
        else:
            return scnd_data