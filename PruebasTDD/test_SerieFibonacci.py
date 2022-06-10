import pytest

from SerieFibonacci import calcularSerie

#0,1,1,2,3,5,8,13...

def test_fibonacciError():
    numero=1
    assert calcularSerie(numero) == 0

def test_fibonacci_1():
    numero = 1
    assert calcularSerie(numero) == 0

def test_fibonacci_6():
    numero = 6
    assert calcularSerie(numero) == 5

@pytest.mark.parametrize(
    "nueroDeEntrada , valorEsperado",
    [
        (1,0),
        (2,1),
        (3,1),
        (4,2),
        (5,3),
        (6,5),
        (7,8),
        (8,13)
    ]
    

)
def test_fibonacci_Multi(nueroDeEntrada , valorEsperado):
    assert calcularSerie(nueroDeEntrada) == valorEsperado

