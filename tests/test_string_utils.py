import pytest
from utils.string_utils import capitalize_last_letter, capitalize_first_and_last_letter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        # Test case for a simple lowercase string
        ("hello", "HellO"),
        # Test case for a mixed case string
        ("hElLo", "HElLO"),
        # Test case for a 2-character string
        ("ab", "AB"),
        # [Tusk] FAILING TEST
        # Test case for a single character string
        ("a", "A"),
    ],
)
def test_capitalize_first_and_last_letter(input_string, expected_output):
    """
    Tests that capitalize_first_and_last_letter correctly capitalizes the first and last characters of a string.
    """
    # WHEN the capitalize_first_and_last_letter function is called with the input string
    result = capitalize_first_and_last_letter(input_string)

    # THEN the result should match the expected output
    assert result == expected_output


def test_capitalize_first_and_last_letter_empty_string():
    """
    Tests that capitalize_first_and_last_letter raises an IndexError when called with an empty string.
    """
    # WHEN the capitalize_first_and_last_letter function is called with an empty string
    with pytest.raises(IndexError):
        capitalize_first_and_last_letter("")

    # THEN an IndexError should be raised


def test_capitalize_first_and_last_letter_type_error():
    """
    Tests that capitalize_first_and_last_letter raises a TypeError when called with a non-string input.
    """
    with pytest.raises(TypeError):
        capitalize_first_and_last_letter(123)


def test_capitalize_first_and_last_letter_multi_word():
    """
    Tests that capitalize_first_and_last_letter correctly capitalizes the first and last characters of a multi-word string.
    """
    # GIVEN a multi-word string
    input_string = "hello world"

    # WHEN the capitalize_first_and_last_letter function is called with the input string
    result = capitalize_first_and_last_letter(input_string)

    # THEN the result should have the first and last characters capitalized
    assert result == "Hello worlD"


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (" ", " "),
        ("\t", "\t"),
        ("\n", "\n"),
        ("  ", "  "),
        ("\t\t", "\t\t"),
        ("\n\n", "\n\n"),
        (" \t\n", " \t\n"),
    ],
)
def test_capitalize_last_letter_whitespace_string(input_string, expected_output):
    """
    Tests that capitalize_last_letter correctly handles strings containing only whitespace characters.
    """
    # WHEN the capitalize_last_letter function is called with the input string
    result = capitalize_last_letter(input_string)

    # THEN the result should match the expected output
    assert result == expected_output


def test_capitalize_last_letter_unicode_emoji():
    """
    Tests that capitalize_last_letter correctly handles a string with a unicode emoji at the end.
    """
    # GIVEN
    input_string = "hello😊"
    expected_output = "hello😊"

    # WHEN
    result = capitalize_last_letter(input_string)

    # THEN
    assert result == expected_output


def test_capitalize_last_letter_non_latin():
    """
    Tests that capitalize_last_letter correctly handles non-latin characters.
    """
    # GIVEN a string with a Chinese character at the end
    input_string = "你好世界"

    # WHEN the capitalize_last_letter function is called with the input string
    result = capitalize_last_letter(input_string)

    # THEN the result should be the same as the input string because the Chinese character doesn't have an uppercase version
    assert result == "你好世" + "界".upper()
