import pytest
from utils.calculator import add, subtract, divide, multiply
from decimal import Decimal


def test_add():
    assert add(1, 2) == 3


def test_subtract_positive_integers():
    """
    Test that subtract returns the correct difference
    when subtracting two positive integers.
    """
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(7, 7) == 0
    assert subtract(100, 1) == 99


def test_subtract_different_numeric_types():
    """
    Test that subtract returns the correct difference
    when subtracting different numeric types.
    """
    assert subtract(5.0, 2) == 3.0
    assert subtract(5, 2.0) == 3.0
    assert subtract(Decimal("5.0"), 2) == Decimal("3.0")
    assert subtract(5, Decimal("2.0")) == Decimal("3.0")
    assert subtract(2, 5.0) == -3.0
    assert subtract(2.0, 5) == -3.0
    assert subtract(Decimal("2.0"), 5) == Decimal("-3.0")
    assert subtract(2, Decimal("5.0")) == Decimal("-3.0")


def test_multiply_positive_integers():
    """
    Test that multiply returns the correct product
    when multiplying two positive integers.
    """
    assert multiply(2, 3) == 6, "Test Case 1 Failed: 2 * 3 should be 6"
    assert multiply(1, 5) == 5, "Test Case 2 Failed: 1 * 5 should be 5"
    assert multiply(10, 20) == 200, "Test Case 3 Failed: 10 * 20 should be 200"
    assert multiply(7, 8) == 56, "Test Case 4 Failed: 7 * 8 should be 56"
    assert multiply(100, 1) == 100, "Test Case 5 Failed: 100 * 1 should be 100"


def test_multiply_positive_and_negative_integers():
    """
    Test that multiply returns the correct product
    when multiplying a positive and a negative integer.
    """
    assert multiply(2, -3) == -6, "Test Case 1 Failed: 2 * -3 should be -6"
    assert multiply(-1, 5) == -5, "Test Case 2 Failed: -1 * 5 should be -5"
    assert multiply(10, -20) == -200, "Test Case 3 Failed: 10 * -20 should be -200"
    assert multiply(-7, 8) == -56, "Test Case 4 Failed: -7 * 8 should be -56"
    assert multiply(100, -1) == -100, "Test Case 5 Failed: 100 * -1 should be -100"
    assert multiply(-1, 100) == -100, "Test Case 6 Failed: -1 * 100 should be -100"


def test_multiply_negative_integers():
    """
    Test that multiply returns the correct product
    when multiplying two negative integers.
    """
    assert multiply(-2, -3) == 6, "Test Case 1 Failed: -2 * -3 should be 6"
    assert multiply(-1, -5) == 5, "Test Case 2 Failed: -1 * -5 should be 5"
    assert multiply(-10, -20) == 200, "Test Case 3 Failed: -10 * -20 should be 200"
    assert multiply(-7, -8) == 56, "Test Case 4 Failed: -7 * -8 should be 56"
    assert multiply(-100, -1) == 100, "Test Case 5 Failed: -100 * -1 should be 100"


def test_divide_floating_point_numbers():
    """
    Test that divide returns the correct quotient
    when dividing two floating-point numbers.
    """
    assert divide(10.0, 2.0) == pytest.approx(5.0)
    assert divide(7.5, 2.5) == pytest.approx(3.0)
    assert divide(1.0, 5.0) == pytest.approx(0.2)
    assert divide(100.5, 10.0) == pytest.approx(10.05)
    assert divide(9.9, 3.0) == pytest.approx(3.3)
    assert divide(1.1, 1.1) == pytest.approx(1.0)
    assert divide(3.14159, 2.0) == pytest.approx(1.570795)


def test_divide_zero_numerator():
    """
    Test that divide returns zero when the numerator is zero.
    """
    assert divide(0, 5) == 0
    assert divide(0, 1) == 0
    assert divide(0, 100) == 0


def test_divide_positive_by_negative():
    """
    Test that divide returns the correct quotient
    when dividing a positive integer by a negative integer.
    """
    assert divide(10, -2) == -5.0
    assert divide(7, -2) == -3.5
    assert divide(1, -5) == -0.2
    assert divide(100, -10) == -10.0
    assert divide(9, -3) == -3.0
    assert divide(1, -1) == -1.0
