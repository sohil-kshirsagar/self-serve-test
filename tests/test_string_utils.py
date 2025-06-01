import pytest
from utils.string_utils import capitalize_first_letter

# Test scenarios for capitalize_first_letter
# Each test function will cover a specific case for capitalize_first_letter.
# This structure allows for clear, focused tests and makes it easy to add new ones.


def test_capitalize_first_letter_simple_lowercase():
    """
    Test that capitalize_first_letter correctly capitalizes the first letter
    of a simple lowercase word.
    """
    input_string = "hello"
    expected_output = "Hello"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_already_capitalized():
    """
    Test that capitalize_first_letter returns the same string when the first letter is already capitalized.
    """
    input_string = "Hello"
    expected_output = "Hello"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_single_char_lowercase():
    """
    Test that capitalize_first_letter correctly capitalizes the first letter
    of a single lowercase character.
    """
    input_string = "h"
    expected_output = "H"
    assert capitalize_first_letter(input_string) == expected_output


# [Tusk] FAILING TEST
def test_capitalize_first_letter_mixed_case():
    """
    Test that capitalize_first_letter correctly capitalizes the first letter
    of a mixed case word, keeping the rest of the string unchanged.
    """
    input_string = "hELLO"
    expected_output = "Hello"
    assert capitalize_first_letter(input_string) == expected_output


# [Tusk] FAILING TEST
def test_capitalize_first_letter_leading_space():
    """
    Test that capitalize_first_letter correctly capitalizes the first letter
    of a string with leading spaces.
    """
    input_string = " hello"
    expected_output = " Hello"
    assert capitalize_first_letter(input_string) == expected_output


# Future tests for capitalize_first_letter can be added below, for example:
#
# def test_capitalize_first_letter_mixed_case():
#     assert capitalize_first_letter("hELLO") == "Hello"
#
# def test_capitalize_first_letter_leading_space():
#     # Based on current implementation, this would become " Hello"
#     # If behavior should be different (e.g. trim then capitalize), test would change
#     assert capitalize_first_letter(" hello") == " Hello"
#
# def test_capitalize_first_letter_empty_string():
#     # This test would currently fail with an IndexError.
#     # It's included here as a placeholder for when the function is updated
#     # to handle empty strings gracefully, as mentioned in "Additional test scenarios".
#     # with pytest.raises(IndexError): # Or assert specific graceful handling
#     #     capitalize_first_letter("")
#     pass # Placeholder until graceful handling is implemented
