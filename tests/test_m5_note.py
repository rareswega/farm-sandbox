import pytest

def test_m5_note():
    with open('notes/m5.txt', 'r') as f:
        content = f.read()
    assert content == 'farm-m5\n'
