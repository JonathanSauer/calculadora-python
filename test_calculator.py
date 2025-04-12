import calculator

def test_somar():
    assert calculator.somar(2, 3) == 5

def test_subtrair():
    assert calculator.subtrair(5, 3) == 2

def test_multiplicar():
    assert calculator.multiplicar(2, 4) == 8

def test_dividir():
    assert calculator.dividir(10, 2) == 5