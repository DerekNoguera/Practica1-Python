import pytest
from unittest.mock import Mock, patch
from biblioteca import Biblioteca, Libro

@pytest.fixture
def biblioteca():
    libros = [Libro('test', 'test', 5)]
    return Biblioteca(libros)

def test_prestar_libro(biblioteca):
    biblioteca.buscar_libro = Mock('test')
    biblioteca.prestar_libro('test')
    biblioteca.buscar_libro.return_value.prestar.assert_called_once_with() #asegura que se llama prestar libro de la clase libro
    
    biblioteca.prestar_libro = Mock('test')
    biblioteca.prestar_libro('test')
    biblioteca.prestar_libro.assert_called_once_with('test') #asegura que se llama prestar libro de la clase biblioteca
    
@patch.object(Biblioteca, 'buscar_libro')
def test_prestar_libro_with(mock_buscar_libro, biblioteca):
    with patch.object(Biblioteca, 'prestar_libro') as mock_prestar_libro:
        biblioteca.prestar_libro('test')
        mock_prestar_libro.assert_called_once_with('test')
    
    biblioteca.prestar_libro('test')
    mock_buscar_libro.return_value.prestar.assert_called_once_with()
   
@patch.object(Biblioteca, 'buscar_libro')
@patch.object(Biblioteca, 'prestar_libro')
def test_prestar_libro_with_error(mock_buscar_libro, mock_prestar_libro, biblioteca):
    biblioteca.prestar_libro('test')
    mock_buscar_libro.assert_called_once_with('test')
    mock_buscar_libro.return_value.prestar.assert_called_once_with()