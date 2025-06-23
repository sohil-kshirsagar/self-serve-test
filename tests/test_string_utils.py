import pytest
from utils.string_utils import capitalize_last_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        # Test case for a simple lowercase string
        ("hello", "hellO"),
        # Test case for a single character string
        ("a", "A"),
        # Test case for a mixed case string
        ("hElLo", "hElLO"),
        # Test case with a number at the end
        ("123", "123"),
        # Test case with a special character at the end
        ("hello!", "hello!"),
    ],
)
def test_capitalize_last_letter(input_string, expected_output):
    """
    Tests that capitalize_last_letter correctly capitalizes the final character of a string.
    """
    # WHEN the capitalize_last_letter function is called with the input string
    result = capitalize_last_letter(input_string)

    # THEN the result should match the expected output
    assert result == expected_output


def test_capitalize_last_letter_empty_string():
    """
    Tests that capitalize_last_letter raises an IndexError when called with an empty string.
    """
    # WHEN the capitalize_last_letter function is called with an empty string
    with pytest.raises(IndexError):
        capitalize_last_letter("")

    # THEN an IndexError should be raised


def test_capitalize_last_letter_type_error():
    """
    Tests that capitalize_last_letter raises a TypeError when called with a non-string input.
    """
    with pytest.raises(TypeError):
        capitalize_last_letter(123)
