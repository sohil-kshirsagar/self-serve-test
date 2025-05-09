import pytest
from utils.calculator import add, subtract, divide
import sys


def test_add():
    assert add(1, 2) == 3


def test_subtract_positive_integers():
    assert subtract(5, 3) == 2


def test_subtract_zero():
    assert subtract(5, 0) == 5


def test_subtract_negative_and_positive_integers():
    assert subtract(-5, 3) == -8


def test_subtract_negative_integers():
    assert subtract(-5, -3) == -2


def test_subtract_floating_point_numbers():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)


def test_subtract_invalid_input():
    with pytest.raises(TypeError):
        subtract("a", 1)


def test_subtract_large_integers():
    large_number = sys.maxsize
    small_number = 1000
    assert subtract(large_number, small_number) == large_number - small_number


def test_subtract_floating_point_precision():
    a = 0.1 + 0.2
    b = 0.3
    assert subtract(a, b) == pytest.approx(0.0)


def test_divide_positive_integers():
    assert divide(10, 2) == 5


def test_divide_negative_numerator():
    assert divide(-10, 2) == -5


def test_divide_negative_integers():
    assert divide(-10, -2) == 5


def test_divide_zero_numerator():
    assert divide(0, 5) == 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_divide_repeating_decimal():
    assert abs(divide(1, 3) - 0.333333333) < 1e-9


def test_divide_large_numbers():
    large_number = 2**100  # A large number, but still manageable
    assert divide(large_number, 2) == large_number / 2


def test_divide_small_denominator():
    assert divide(1, 0.0000001) == 10000000.0
