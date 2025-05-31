import pytest
from utils.string_utils import capitalize_first_letter

# Test cases for capitalize_first_letter
# Each tuple represents (input_string, expected_output)
capitalize_test_cases = [
    ("hello", "Hello"),
    ("Hello", "Hello"),
    ("a", "A"),
    ("a123", "A123"),
    # [Tusk] FAILING TEST
    ("hELLO", "Hello"),
    # Future test scenarios will be added here, for example:
    # ("hELLO", "Hello"),
]


@pytest.mark.parametrize("input_string, expected_output", capitalize_test_cases)
def test_capitalize_first_letter_scenarios(input_string, expected_output):
    """
    Tests the capitalize_first_letter function with various scenarios.
    """
    assert capitalize_first_letter(input_string) == expected_output


# Placeholder for tests for empty string or non-alphabetic starting characters,
# which might require different assertions (e.g., expecting errors or specific handling).
# These will be added as separate test functions or parameterized cases as appropriate.


def test_capitalize_first_letter_empty_string():
    # Assuming the current implementation raises IndexError for empty string,
    # and we want to test that behavior before any potential fix.
    # Or, if it's fixed, this test would change.
    with pytest.raises(IndexError):  # Or a custom error if defined
        capitalize_first_letter("")


def test_capitalize_first_letter_non_string_input():
    with pytest.raises((TypeError, AttributeError)):
        capitalize_first_letter(None)
    with pytest.raises((TypeError, AttributeError)):
        capitalize_first_letter(123)


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("123abc", "123abc"),
        ("#hello", "#hello"),
        (" hello", " hello"),
    ],
)
def test_capitalize_first_letter_non_alphabetic_start(input_string, expected_output):
    """
    Tests the capitalize_first_letter function when the input string starts with a non-alphabetic character.
    """
    assert capitalize_first_letter(input_string) == expected_output
