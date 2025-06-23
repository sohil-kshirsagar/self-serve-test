import pytest
from utils.string_utils import capitalize_last_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        # Test case for a simple lowercase string
        ("hello", "hellO"),
        # Test case for a single character string
        ("a", "A"),
        # Test case for a mixed-case string
        ("hElLo", "hElLO"),
        # Test case where the last character is a number
        ("hello123", "hello123"),
        # Test case where the last character is a symbol
        ("test!", "test!"),
        # Test case where the last character is whitespace
        ("word ", "word "),
    ],
)
def test_capitalize_last_letter(input_string, expected_output):
    """
    Tests the capitalize_last_letter function with various inputs.
    """
    assert capitalize_last_letter(input_string) == expected_output


def test_capitalize_last_letter_non_string_input():
    """
    Tests that capitalize_last_letter raises a TypeError when given a non-string input.
    """
    with pytest.raises(TypeError):
        capitalize_last_letter(123)
