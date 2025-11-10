import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected_output", [
    ("skypro", "Skypro"), ("hello world", "Hello world"), ("589", "589")
])
def test_capitalize_positive(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.capitalize(input_str)
    assert result == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    ("675tre", "675tre"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.capitalize(input_str)
    assert result == expected_output


import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected_output", [
    ("   hello", "hello"),
    ("hello", "hello")
])
def test_trim_positive(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.trim(input_str)
    assert result == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    ("", ""),
    (" ", ""),
])
def test_trim_negative(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.trim(input_str)
    assert result == expected_output


import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected_output", [
    ("Hello", "H"),
    ("SkyPro", "S")
])
def test_contains_positive(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.contains(input_str, expected_output)
    assert result is True


@pytest.mark.parametrize("input_str, expected_output", [
    ("SkyPro", "F"),
    ("Hello", "O"),
])
def test_contains_negative(input_str, expected_output):
    string_utils = StringUtils()
    result = string_utils.contains(input_str, expected_output)
    assert result is False


import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize("string, symbol, expected_result", [
    ("Hello", "H", "ello"),
    ("SkyPro", "P", "Skyro")
])
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result


@pytest.mark.parametrize("string, symbol, expected_result", [
    ("SkyPro", "L", "SkyPro")
])
def test_delete_symbol_negative(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
