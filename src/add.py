def summ_number(a,b):
    return a + b

def divide_num(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено")
    return a / b
