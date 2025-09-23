import pytest
import os
import sys
import tempfile

#Import task4 function
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task6 import countWords

# Test to make sure the word count is correct for content file
def testCountWords():
    assert countWords("/home/student/sanchezCS4300/homework1/task6_read_me.txt") == 127

import pytest

# same test but parametrized
@pytest.mark.parametrize("textContent, expected_count", [
    ("/home/student/sanchezCS4300/homework1/task6_read_me.txt", 127),
])
def test_count_words(textContent, expected_count):
    assert countWords(textContent) == expected_count

