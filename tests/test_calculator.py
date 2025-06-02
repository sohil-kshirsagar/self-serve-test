import pytest
from utils.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


def test_subtract_positive_integers():
    """
    Test that subtract returns the correct result when subtracting
    two positive integers.
    """
    # Arrange
    minuend = 10
    subtrahend = 3
    expected_difference = 7

    # Act
    actual_difference = subtract(minuend, subtrahend)

    # Assert
    assert actual_difference == expected_difference

    # Another example with different positive integers
    minuend_2 = 5
    subtrahend_2 = 5
    expected_difference_2 = 0
    actual_difference_2 = subtract(minuend_2, subtrahend_2)
    assert actual_difference_2 == expected_difference_2

    # Example where subtrahend is larger
    minuend_3 = 2
    subtrahend_3 = 8
    expected_difference_3 = -6
    actual_difference_3 = subtract(minuend_3, subtrahend_3)
    assert actual_difference_3 == expected_difference_3


def test_subtract_negative_integers():
    """
    Test that subtract returns the correct result when subtracting
    two negative integers.
    """
    # Arrange
    minuend = -5
    subtrahend = -2
    expected_difference = -3

    # Act
    actual_difference = subtract(minuend, subtrahend)

    # Assert
    assert actual_difference == expected_difference

    # Another example with different negative integers
    minuend_2 = -10
    subtrahend_2 = -5
    expected_difference_2 = -5
    actual_difference_2 = subtract(minuend_2, subtrahend_2)
    assert actual_difference_2 == expected_difference_2

    # Example where subtrahend is larger in magnitude
    minuend_3 = -2
    subtrahend_3 = -8
    expected_difference_3 = 6
    actual_difference_3 = subtract(minuend_3, subtrahend_3)
    assert actual_difference_3 == expected_difference_3


def test_subtract_positive_and_negative_integers():
    """
    Test that subtract returns the correct result when subtracting
    a negative integer from a positive integer.
    """
    # Arrange
    positive_number = 10
    negative_number = -5
    expected_result = 15

    # Act
    actual_result = subtract(positive_number, negative_number)

    # Assert
    assert actual_result == expected_result


def test_multiply_positive_integers():
    """
    Test that multiply returns the correct product when multiplying
    two positive integers.
    """
    # Arrange Case 1
    num1_case1 = 2
    num2_case1 = 3
    expected_product_case1 = 6

    # Act Case 1
    actual_product_case1 = multiply(num1_case1, num2_case1)

    # Assert Case 1
    assert (
        actual_product_case1 == expected_product_case1
    ), "Test Case 1 Failed: 2 * 3 should be 6"

    # Arrange Case 2
    num1_case2 = 5
    num2_case2 = 10
    expected_product_case2 = 50

    # Act Case 2
    actual_product_case2 = multiply(num1_case2, num2_case2)

    # Assert Case 2
    assert (
        actual_product_case2 == expected_product_case2
    ), "Test Case 2 Failed: 5 * 10 should be 50"

    # Arrange Case 3: Multiplication by 1
    num1_case3 = 1
    num2_case3 = 7
    expected_product_case3 = 7

    # Act Case 3
    actual_product_case3 = multiply(num1_case3, num2_case3)

    # Assert Case 3
    assert (
        actual_product_case3 == expected_product_case3
    ), "Test Case 3 Failed: 1 * 7 should be 7"

    # Arrange Case 4: Larger positive integers
    num1_case4 = 100
    num2_case4 = 200
    expected_product_case4 = 20000

    # Act Case 4
    actual_product_case4 = multiply(num1_case4, num2_case4)

    # Assert Case 4
    assert (
        actual_product_case4 == expected_product_case4
    ), "Test Case 4 Failed: 100 * 200 should be 20000"


def test_multiply_with_zero():
    """
    Test that multiply returns zero when one of the inputs is zero.
    """
    # Arrange Case 1: Multiplying a positive number by zero
    num1_case1 = 5
    num2_case1 = 0
    expected_product_case1 = 0

    # Act Case 1
    actual_product_case1 = multiply(num1_case1, num2_case1)

    # Assert Case 1
    assert (
        actual_product_case1 == expected_product_case1
    ), "Test Case 1 Failed: 5 * 0 should be 0"

    # Arrange Case 2: Multiplying zero by a positive number
    num1_case2 = 0
    num2_case2 = 10
    expected_product_case2 = 0

    # Act Case 2
    actual_product_case2 = multiply(num1_case2, num2_case2)

    # Assert Case 2
    assert (
        actual_product_case2 == expected_product_case2
    ), "Test Case 2 Failed: 0 * 10 should be 0"

    # Arrange Case 3: Multiplying zero by zero
    num1_case3 = 0
    num2_case3 = 0
    expected_product_case3 = 0

    # Act Case 3
    actual_product_case3 = multiply(num1_case3, num2_case3)

    # Assert Case 3
    assert (
        actual_product_case3 == expected_product_case3
    ), "Test Case 3 Failed: 0 * 0 should be 0"


def test_divide_positive_integers():
    """
    Test that divide returns the correct quotient when dividing
    two positive integers.
    """
    # Arrange
    numerator = 10
    denominator = 2
    expected_quotient = 5.0

    # Act
    actual_quotient = divide(numerator, denominator)

    # Assert
    assert actual_quotient == expected_quotient

    # Another example with positive integers resulting in a non-integer quotient
    # Arrange
    numerator_2 = 7
    denominator_2 = 2
    expected_quotient_2 = 3.5

    # Act
    actual_quotient_2 = divide(numerator_2, denominator_2)

    # Assert
    assert actual_quotient_2 == expected_quotient_2

    # Example with larger positive integers
    # Arrange
    numerator_3 = 100
    denominator_3 = 4
    expected_quotient_3 = 25.0

    # Act
    actual_quotient_3 = divide(numerator_3, denominator_3)

    # Assert
    assert actual_quotient_3 == expected_quotient_3
