import pytest
from utils.string_utils import capitalize_last_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "hellO"),
        ("Hello123Worldz", "Hello123WorldZ"),
    ],
)
def test_capitalize_last_letter_happy_path(input_string, expected_output):
    """
    Tests that capitalize_last_letter correctly capitalizes the last letter
    of a lowercase string.
    """
    # Act: Call the function with the input string
    result = capitalize_last_letter(input_string)

    # Assert: Verify the result matches the expected output
    assert result == expected_output


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hellO", "hellO"),
    ],
)
def test_capitalize_last_letter_already_uppercase(input_string, expected_output):
    """
    Tests that capitalize_last_letter returns the original string when the last letter is already uppercase.
    """
    # Act: Call the function with the input string
    result = capitalize_last_letter(input_string)

    # Assert: Verify the result matches the expected output
    assert result == expected_output


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello1", "hello1"),
    ],
)
def test_capitalize_last_letter_non_alphabetic_last_char(input_string, expected_output):
    """
    Tests that capitalize_last_letter leaves the string unchanged if the last character is non-alphabetic.
    """
    # Act: Call the function with the input string
    result = capitalize_last_letter(input_string)

    # Assert: Verify the result matches the expected output
    assert result == expected_output


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("a", "A"),
    ],
)
def test_capitalize_last_letter_single_character(input_string, expected_output):
    """
    Tests that capitalize_last_letter correctly handles a single character string.
    """
    # Act: Call the function with the input string
    result = capitalize_last_letter(input_string)

    # Assert: Verify the result matches the expected output
    assert result == expected_output
