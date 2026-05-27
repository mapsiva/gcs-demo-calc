from calculadora.calc import somar, subtrair

def test_somar_inteiros ():
    assert somar (2, 3) == 5

def test_somar_negativos ():
    assert somar (-1, -4) == -5

def test_subtrair ():
    assert subtrair (10, 4) == 6