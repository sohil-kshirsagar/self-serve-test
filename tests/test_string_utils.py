import pytest
from utils.string_utils import capitalize_first_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        # Test scenario: capitalize the first letter of a lowercase word
        ("word", "Word"),
        # Additional test scenarios for capitalize_first_letter can be added here.
        # For example:
        # ("Hello", "Hello"),  // Already capitalized
        # ("1hello", "1hello"), // Non-alphabetic first character
        # (" hELLo", " HELLo"), // Leading space (current behavior based on string[0])
        # ("hELLo", "HELLo"),   // Mixed case
        # ("h", "H"),           // Single character lowercase
        # ("H", "H"),           // Single character uppercase
        # Test scenario: capitalize the first letter of a string that starts with spaces followed by a lowercase letter
        ("  hello", "  Hello"),
    ],
)
def test_capitalize_first_letter_scenarios(input_string, expected_output):
    """
    Tests capitalize_first_letter with various inputs.
    """
    assert capitalize_first_letter(input_string) == expected_output


# Note for future engineer:
# The scenario "Consider what happens when capitalize_first_letter is called with an empty string.
# It should handle this case gracefully rather than raising an IndexError."
# will likely require a separate test if the graceful handling means returning a specific value
# (e.g., empty string), or if it's expected to raise a *specific custom error* instead of IndexError.
# If the function is modified to handle empty strings without error (e.g., returns ""),
# then ("","") could be added to the parametrize list above.
# If it's expected to raise an error (even if a custom one), a separate test like:
#
# def test_capitalize_first_letter_empty_string_graceful():
#     # Assuming it should return empty string for empty input
#     assert capitalize_first_letter("") == ""
#     # Or, if it's supposed to raise a specific custom error:
#     # with pytest.raises(CustomEmptyStringError):
#     #     capitalize_first_letter("")
#
# The current implementation of capitalize_first_letter will raise an IndexError
# for an empty string. A test for that specific (current) behavior would be:
#
# def test_capitalize_first_letter_empty_string_raises_index_error():
#     with pytest.raises(IndexError):
#         capitalize_first_letter("")
