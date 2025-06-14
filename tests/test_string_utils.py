import pytest
from utils.string_utils import capitalize_last_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "hellO"),
        ("hellO", "hellO"),  # Last letter already capitalized
        ("a", "A"),
        ("hElLo", "hElLO"),
        ("hello world", "hello worlD"),
        ("test!", "test!"),
        ("word ", "word "),
        # Future test cases for capitalize_last_letter can be added here:
        # e.g., ("hello123", "hello123"),
    ],
)
def test_capitalize_last_letter_various_strings(input_string, expected_output):
    """
    Tests capitalize_last_letter with various string inputs.
    This includes:
    - Standard lowercase string (e.g., "hello" -> "hellO")
    - Strings where the last letter is already capitalized
    - Single character strings
    - Mixed-case strings
    - Strings with spaces
    - Strings where the last character is not a letter
    """
    assert capitalize_last_letter(input_string) == expected_output


def test_capitalize_last_letter_empty_string():
    with pytest.raises(IndexError):
        capitalize_last_letter("")


def test_capitalize_last_letter_non_string_input_int():
    with pytest.raises(TypeError):
        capitalize_last_letter(123)


def test_capitalize_last_letter_non_string_input_none():
    with pytest.raises(TypeError):
        capitalize_last_letter(None)
