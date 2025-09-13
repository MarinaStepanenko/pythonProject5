from typing import List


def get_one_list(list1: List[int], list2: List[int]) -> List[int]:
    """
    Написать функцию, которая получает на вход два списка чисел и
    возвращает новый список,
    содержащий только те числа, которые встречаются в обоих списках.
    """
    common_elements = set(list1).intersection(set(list2))
    return f"{list(common_elements)}"


print(get_one_list([1, 2, 3, 4], [3, 4, 5, 6]))


def get_palindrome(list: List[int]) -> List[int]:
    """
    Написать функцию, которая получает на вход список чисел
    и возвращает новый список, содержащий только числа, которые
    являются палиндромами.
    """
    palidrome = []
    for i in list:
        if str(i)[::-1] == str(i):
            palidrome.append(i)
    return palidrome


print(get_palindrome([121, 123, 131, 34543]))


def circle_area(r: float) -> float:
    pi = 3.14
    circle_area = pi * r ** 2
    return circle_area


def format_description(r: float, area: float):
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_circle_info(r: float) -> None:
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


if __name__ == "__exercise__":
    radius = int(input("Enter circle radius (int): "))
    get_info(radius)
