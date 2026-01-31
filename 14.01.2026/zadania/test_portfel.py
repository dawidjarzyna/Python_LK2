import pytest
from portfel import Portfel

# Pytest uruchomi tę funkcję przed każdym testem, który poprosi o 'pusty_portfel'.
@pytest.fixture
def pusty_portfel():
    return Portfel()

# Test 1: Sprawdzenie salda początkowego
# Przekazujemy nazwę fixture jako argument funkcji!
def test_poczatkowego_salda(pusty_portfel):
    assert pusty_portfel.saldo == 0  

# Test 2: Sprawdzenie wpłaty
# Tutaj również dostajemy świeżą instancję 'pusty_portfel'
def test_wplaty_do_portfela(pusty_portfel):
    pusty_portfel.wplac(100)
    assert pusty_portfel.saldo == 100