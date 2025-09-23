import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task1 import helloWorld

def testConfirmation():
    assert helloWorld()  == "Hello, World!"




