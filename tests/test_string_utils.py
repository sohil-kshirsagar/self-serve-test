import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_simple_lowercase():
    """
    Tests that capitalize_first_letter correctly capitalizes the first letter
    of a simple lowercase word.
    """
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_already_capitalized():
    """
    Tests that capitalize_first_letter returns the same string when the first
    letter is already capitalized.
    """
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_first_letter_mixed_case():
    """
    Tests that capitalize_first_letter correctly capitalizes the first letter
    of a mixed-case word, leaving the other letters unchanged.
    """
    assert capitalize_first_letter("hELLO") == "Hello"


def test_capitalize_first_letter_single_character():
    """
    Tests that capitalize_first_letter correctly capitalizes the first letter
    of a single character string.
    """
    assert capitalize_first_letter("a") == "A"


def test_capitalize_first_letter_already_capital():
    """
    Tests that capitalize_first_letter returns the same string when the first
    letter is already capitalized.
    """
    assert capitalize_first_letter("A") == "A"


def test_capitalize_first_letter_empty_string():
    """
    Tests that capitalize_first_letter raises an IndexError when called with an empty string.
    """
    with pytest.raises(IndexError):
        capitalize_first_letter("")


def test_capitalize_first_letter_number():
    """
    Tests that capitalize_first_letter correctly handles a string
    that starts with a number.
    """
    assert capitalize_first_letter("123hello") == "123hello"


def test_capitalize_first_letter_special_character():
    """
    Tests that capitalize_first_letter correctly handles a string
    that starts with a special character.
    """
    assert capitalize_first_letter("!hello") == "!hello"
