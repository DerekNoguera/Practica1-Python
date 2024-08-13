import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def append_primero(order):
    order.append(1)


@pytest.fixture
def append_segundo(order, append_primero):
    order.extend([2])


@pytest.fixture(autouse=True)
def append_tercero(order, append_segundo):
    order += [3]


def test_order(order):
    assert order == [1, 2, 3]