import pytest
from calcular_promedio import calcular_promedio

def test_promedio_de_lista_vacia():
    assert calcular_promedio([]) == 0
    

def test_promedio_de_lista_con_numeros_positivos():
    assert calcular_promedio([1,2,3,4,5]) == 3
    
def test_promedio_de_lista_con_numeros_negativos():
    assert calcular_promedio([-1,-2,-3,-4,-5]) == -3
    
def test_promedio_de_lista_con_numeros_mixtos():
    pytest.approx(calcular_promedio([1,-2,3,-4,5]), 0.6)