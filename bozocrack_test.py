import pytest
import bozocrack

def test_format_it():
    result = bozocrack.format_it('hash', 'plaintext')
    expected = 'hash:plaintext'
    assert expected == result
def test_crack_single_hash():
    result = bozocrack.crack_single_hash('fcf1eed8596699624167416a1e7e122e')
    expected = 'octopus'
    assert expected == result
