import pytest
from utils.string_utils import capitalize_last_lettr


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        # Scenario: capitalize the last letter of a single word.
        ("hello", "hellO"),
    ],
)
def test_capitalize_last_letter_single_word(input_string, expected_output):
    """
    Tests that capitalize_last_letter correctly capitalizes the last letter of a given string.
    """
    # When the capitalize_last_letter function is called with the input string
    result = capitalize_last_letter(input_string)

    # Then the result should match the expected output
    assert result == expected_output
