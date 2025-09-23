import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task7 import githubUser

# Test to see if a valid username is pulled and assert confirmation
def test_valid_user():
    user_data = githubUser("SyntaxSanchez")  # SyntaxSanchez is a valid GitHub username
    assert user_data is not None
    assert user_data["login"] == "SyntaxSanchez"

# Test to see if a invalid username is pulled and assert confirmation
def test_invalid_user():
    user_data = githubUser("NOTAREALUSERNAME24234254534534")
    assert user_data is None

