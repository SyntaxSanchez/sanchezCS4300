# test_task5.py
import pytest
from task5 import booksThree, studentID

# Test to assert the first three box were pulled from the list
def testBooksThree():
    expected = [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("Brave New World", "Aldous Huxley")
    ]
    assert booksThree() == expected

# Test to assert the student names are applied to the correct ID
def testStudentID():
    assert studentID("Alice") == "S1"
    assert studentID("Chris") == "S2"
    assert studentID("Jessie") == "S3"
    assert studentID("Diana") == "S4"
    assert studentID("Unknown") is None

