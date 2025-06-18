import pytest
from utils.string_utils import capitalize_last_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "hellO"),
        ("hellO", "hellO"),
        ("a", "A"),
        ("HELLO", "HELLO"),
        ("hElLo", "hElLO"),
        ("123", "123"),
        ("hello!", "hello!"),
        ("test ", "test "),
        ("café", "cafÉ"),
        ("naïve", "naïvE"),
        # Future test scenarios for capitalize_last_letter can be added here:
    ],
)
def test_capitalize_last_letter(input_string, expected_output):
    """
    Tests the capitalize_last_letter function with various inputs.
    """
    assert capitalize_last_letter(input_string) == expected_output


def test_capitalize_last_letter_empty_string():
    with pytest.raises(IndexError):
        capitalize_last_letter("")
