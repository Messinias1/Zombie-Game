from currency import Currency
import pytest


def test_initialize_coin():
    coin = Currency()
    assert coin.Value()==(0)

def test_add_coin():
    coin = Currency()
    coin.add(101)
    assert coin.Value()==(101)
        
def test_remove_coin():
    coin = Currency()
    coin.add(100)
    coin.subtract(50)
    assert coin.Value()==(50)

def test_coin_overflow():
    coin = Currency()
    coin.add(9999)
    coin.add(99)
    assert coin.Value()==(9999)

def test_coin_negative():
    coin = Currency()
    with pytest.raises(ValueError):
            coin.subtract(99)

def test_coin_add_noninteger():
    coin = Currency()
    with pytest.raises(TypeError):
        coin.add("9999")

def test_coin_subtract_noninteger():
    coin = Currency()
    with pytest.raises(TypeError):
        coin.subtract("9999")

def test_coin_add_negative():
    coin = Currency()
    with pytest.raises(ValueError):
        coin.add(-10)

def test_coin_subtract_negative():
    coin = Currency()
    with pytest.raises(ValueError):
        coin.subtract(-10)
    

