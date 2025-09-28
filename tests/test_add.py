import pytest
from src.add import summ_number, divide_num

def test_summ_number(a, b):
    assert summ_number(6, 2) == 8

def test_divide_num(number):
    assert divide_num(24, 3) == number
    with pytest.raises(ZeroDivisionError):
        divide_num(6, 0)