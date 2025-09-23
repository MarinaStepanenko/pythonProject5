import pytest

from src.taxes import calculate_taxes

@pytest.fixture
def prices():
    return [121.1, 163.20, 171.6]

@pytest.mark.parametrize("tax_rate, expected",
                         [(14.78, [138.99858, 187.32095999999999, 196.96248]),
                         (15.3, [139.6283, 188.1696, 197.85479999999998])])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected
    # with pytest.raises(ValueError):
    #     calculate_taxes([143.9, 223.0], -1.1) == 'Неверный налоговый процент'
    #     calculate_taxes([192.1, -1, 0], 17.5) == 'Неверная цена'

def test_calculate_taxes_invalid_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1) == 'Неверный налоговый процент'

def test_calcalute_taxes_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([-3, 0], 6) == 'Неверная цена'