import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_lowercase_string():
    """
    Tests that capitalize_first_letter correctly capitalizes the first letter
    of a lowercase string.
    """
    input_string = "hello world"
    expected_output = "Hello world"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_another_lowercase_string():
    """
    Tests with another lowercase string to ensure general applicability.
    """
    input_string = "python"
    expected_output = "Python"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_single_character_string():
    """
    Tests that capitalize_first_letter correctly handles single-character strings.
    """
    input_string = "a"
    expected_output = "A"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_already_capitalized():
    """
    Tests that capitalize_first_letter returns the string unchanged
    if the first letter is already capitalized.
    """
    input_string = "Hello world"
    expected_output = "Hello world"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_with_spaces_and_special_chars():
    """
    Tests that capitalize_first_letter correctly capitalizes the first letter
    when the string contains spaces and special characters after the first letter.
    """
    input_string = " test string!"
    expected_output = " Test string!"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_non_string_input():
    """
    Tests that capitalize_first_letter raises a TypeError when given a non-string input.
    """
    with pytest.raises(TypeError):
        capitalize_first_letter(123)
