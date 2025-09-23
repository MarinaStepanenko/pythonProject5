def diff_between_list(list_one: list[int], list_two: list[int]) -> list:
    """
    Написать функцию, которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа,
    которые есть только в одном из списков.
    """
    diff_list1 = list(set(list_one) - set(list_two)) + list(set(list_two) - set(list_one))
    return diff_list1

print(diff_between_list([1, 2, 3, 4], [3, 4, 5, 6]))
