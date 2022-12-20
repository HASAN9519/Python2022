''' 
Import pytest and modules
'''
import pytest
import myMath

# String variables to be tested
#alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Do not delete this function, may change value assigned to input to test different inputs to test functions
@pytest.fixture
def input_value():
    input = beta
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars
    Use an assert statement to check given string has fewer than 10 words
    Use an assert statement to check given string has fewer than 50 chars
    Args: input_value: a function that returns a string which can be configured in input_value() function
    """
    assert myMath.word_count(input_value) < 10
    assert myMath.char_count(input_value) < 50


# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period
    Use an assert statement to check given string begins with a capital letter
    Use an assert statement to check given string end with a period ('.')
    Args: input_value: a function that returns a string, which can be configured in input_value() function
    """
    assert myMath.first_char(input_value).isupper()
    assert myMath.last_char(input_value).endswith(".")

# Run these tests in terminal: pytest mypytest.py
# run pytest only on specific function by following command: pytest mypytest.py::test_length
