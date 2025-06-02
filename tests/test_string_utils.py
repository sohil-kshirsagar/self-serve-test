import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_single_character_string():
    """
    Tests that capitalize_first_letter correctly handles single-character strings.
    """
    input_string = "a"
    expected_output = "A"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_with_spaces_and_special_chars():
    """
    Tests that capitalize_first_letter correctly capitalizes the first letter
    when the string contains spaces and special characters after the first letter.
    """
    input_string = " test string!"
    expected_output = " Test string!"
    assert capitalize_first_letter(input_string) == expected_output
