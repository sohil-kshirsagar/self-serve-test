import pytest
from utils.string_utils import capitalize_first_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("hello world", "Hello world"),
        ("123abc", "123abc"),
        ("a", "A"),
        # Future test scenarios for capitalize_first_letter will be added here.
        # For example:
        # (" hello", " Hello"),
        # ("!hello", "!hello"), # Assuming no change for non-alphabetic first char
    ],
)
def test_capitalize_first_letter(input_string, expected_output):
    """
    Tests the capitalize_first_letter function with various inputs.
    """
    assert capitalize_first_letter(input_string) == expected_output


def test_capitalize_first_letter_empty_string():
    """
    Tests that capitalize_first_letter raises an IndexError when called with an empty string.
    """
    with pytest.raises(IndexError):
        capitalize_first_letter("")
