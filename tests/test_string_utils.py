import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_already_capitalized_string():
    """
    Test that capitalize_first_letter returns the same string when the input
    already has the first letter capitalized.
    """
    input_string = "Hello world"
    expected_output = "Hello world"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_multi_word_string_only_first_word():
    """
    Test that capitalize_first_letter capitalizes only the first letter of the
    first word when the input is a multi-word string.
    """
    input_string = "this is a test"
    expected_output = "This is a test"
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_non_string_input():
    """
    Test that capitalize_first_letter raises a TypeError when given a non-string input.
    """
    with pytest.raises(TypeError):
        capitalize_first_letter(123)


def test_capitalize_single_character_string():
    """
    Test that capitalize_first_letter correctly capitalizes a single-character string.
    """
    input_string = "a"
    expected_output = "A"
    assert capitalize_first_letter(input_string) == expected_output


# Placeholder for future tests, demonstrating structure:
# def test_capitalize_empty_string():
#     # To be implemented
#     pass
