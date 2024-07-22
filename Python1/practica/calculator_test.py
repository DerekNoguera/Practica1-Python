import calculator

def test_add():
    assert calculator.add(a=2, b=3) == 5
    assert calculator.add(a=0, b=0) == 0
    assert calculator.add(-1, b=1) == 0
def test_subtract():
    assert calculator.subtract(a=5, b=3) == 2
    assert calculator.subtract(a=0, b=0) == 0
    assert calculator.subtract(-1, -1) == 0
def test_multiply():
    assert calculator.multiply(a=2, b=3) == 6
    assert calculator.multiply(a=0, b=0) == 0
    assert calculator.multiply(-1, b=1) == -1
def test_divide():
    assert calculator.divide(a=6, b=3) == 2
    assert calculator.divide(a=10, b=2) == 5
    assert calculator.divide(a=5, b=2) == 2.5
    