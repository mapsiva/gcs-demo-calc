from calculadora.calc import somar, subtrair, multiplicar

def test_somar_inteiros ():
    assert somar (2, 3) == 5

def test_somar_negativos ():
    assert somar (-1, -4) == -5

def test_subtrair ():
    assert subtrair (10, 4) == 6

def test_multiplicar ():
    assert multiplicar (4, 5) == 20

def test_multiplicar_por_zero ():
    assert multiplicar(7, 0) == 0

def test_multiplicar_negativos ():
    assert multiplicar(-3, -3) == 9