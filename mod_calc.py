def sum_data(a, b):
    return a + b


def sub_data(a, b):
    return a - b


def mul_data(a, b):
    return a * b


def div_data(a, b, param="/"):
    if param == "%":
        return round(a % b, 2)
    elif param == "//":
        return a // b
    return a / b


def pow_data(a, b=None):
    if not b:
        return a ** 0.5
    return a ** b