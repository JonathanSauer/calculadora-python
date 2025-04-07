import calculator

def test_add():
    assert calculator.add(3, 2) == 5

def test_subtract():
    assert calculator.subtract(5, 2) == 3

def test_multiply():
    assert calculator.multiply(4, 3) == 12

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    try:
        calculator.divide(5, 0)
    except ValueError:
        assert True
    else:
        assert False