import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task7 import githubUser

def test_valid_user():
    user_data = githubUser("octocat")  # octocat is a valid GitHub username
    assert user_data is not None
    assert user_data["login"] == "octocat"

def test_invalid_user():
    user_data = githubUser("thisuserdoesnotexist1234567890")
    assert user_data is None

