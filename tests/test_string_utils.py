import pytest
from utils.string_utils import capitalize_last_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        # Test case for a simple lowercase string
        ("hello", "hellO"),
        # Test case where the last letter is already capitalized
        ("hellO", "hellO"),
        # Test case for a single character string
        ("a", "A"),
        # Test case for a string that is entirely uppercase except for the last letter
        ("HELLo", "HELLO"),
        # Test case where the last character is a number
        ("hello2", "hello2"),
        # Test case where the last character is a special character
        ("test!", "test!"),
    ],
)
def test_capitalize_last_letter(input_string, expected_output):
    """
    Tests that capitalize_last_letter correctly capitalizes the last letter of a string.
    This parameterized test is designed to be easily extended with more valid string scenarios.
    """
    assert capitalize_last_letter(input_string) == expected_output


def test_capitalize_last_letter_empty_string():
    """
    Tests that capitalize_last_letter raises an IndexError when called with an empty string.
    """
    with pytest.raises(IndexError):
        capitalize_last_letter("")
