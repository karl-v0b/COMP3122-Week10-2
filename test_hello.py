import pytest
from hello import *

def test_add():
    assert add(3,4)==7

def test_sub():
    assert sub(3,4)==-1
