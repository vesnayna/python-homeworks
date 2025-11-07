import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected_output", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("589", "589")
])
def test_capitalize(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.capitalize(input_str)
    assert result == expected_output


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_output", [
    ("675tre", "675tre"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.capitalize(input_str)
    assert result == expected_output