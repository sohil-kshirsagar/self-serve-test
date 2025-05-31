import pytest
from utils.string_utils import capitalize_first_letter

# hello

def test_capitalize_first_letter_simple_lowercase():
    """
    Test that capitalize_first_letter correctly capitalizes the first letter
    of a simple lowercase word.
    """
    input_string = "hello"
    expected_output = "Hello"
    actual_output = capitalize_first_letter(input_string)
    assert actual_output == expected_output


def test_capitalize_first_letter_already_capitalized():
    """
    Test that capitalize_first_letter returns the same string when the first
    letter is already capitalized.
    """
    input_string = "Hello"
    expected_output = "Hello"
    actual_output = capitalize_first_letter(input_string)
    assert actual_output == expected_output


def test_capitalize_first_letter_mixed_case():
    """
    Test that capitalize_first_letter correctly capitalizes the first letter
    of a mixed case word.
    """
    input_string = "helloWorld"
    expected_output = "HelloWorld"
    actual_output = capitalize_first_letter(input_string)
    assert actual_output == expected_output


def test_capitalize_first_letter_single_character():
    """
    Test that capitalize_first_letter correctly capitalizes a single character.
    """
    input_string = "a"
    expected_output = "A"
    actual_output = capitalize_first_letter(input_string)
    assert actual_output == expected_output


def test_capitalize_first_letter_already_capitalized_single_char():
    """
    Test that capitalize_first_letter returns the same string when the first
    letter is already capitalized.
    """
    input_string = "A"
    expected_output = "A"
    actual_output = capitalize_first_letter(input_string)
    assert actual_output == expected_output


def test_capitalize_first_letter_empty_string():
    """
    Test that capitalize_first_letter raises an IndexError when called with an empty string.
    """
    input_string = ""
    with pytest.raises(IndexError):
        capitalize_first_letter(input_string)


def test_capitalize_first_letter_non_string_input():
    """
    Test that capitalize_first_letter raises a TypeError when called with a non-string argument.
    """
    with pytest.raises(TypeError):
        capitalize_first_letter(123)

    with pytest.raises(TypeError):
        capitalize_first_letter(None)


def test_capitalize_first_letter_non_alpha_start():
    """
    Test that capitalize_first_letter correctly handles strings that start
    with a non-alphabetic character.
    """
    input_string = "123hello"
    expected_output = "123hello"
    actual_output = capitalize_first_letter(input_string)
    assert actual_output == expected_output
