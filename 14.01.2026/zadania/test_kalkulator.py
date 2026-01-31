# test_kalkulator.py
import pytest
from kalkulator import dodaj, dziel

# # --- Testy z Zadania 1 ---

def test_dodawania_liczb_dodatnich():
    assert dodaj(2, 3) == 5

def test_dodawania_liczb_ujemnych():
    assert dodaj(-1, -1) == -2

# # --- Testy z Zadania 2 (Nowe) ---

def test_dzielenia_przez_zero_powinno_rzucic_blad():
    # Używamy menedżera kontekstu (with) żeby sprawdzić, czy błąd faktycznie wystąpił
    with pytest.raises(ValueError):
        dziel(10, 0)

def test_poprawnego_dzielenia():
    # Opcjonalny test sprawdzający normalne działanie
    assert dziel(10, 2) == 5


#--------------------------
# test_kalkulator.py
#--------------------------
# import pytest
# from kalkulator import dodaj, dziel

# --- ZADANIE 4: Parametryzacja ---

# Dekorator definiuje nazwy zmiennych ("a, b, wynik") oraz listę przypadków testowych.
# Pytest uruchomi funkcję poniżej 4 razy - raz dla każdego wiersza danych.
@pytest.mark.parametrize("a, b, oczekiwany_wynik", [
    (2, 3, 5),          # Dwie liczby dodatnie
    (-2, -3, -5),       # Dwie liczby ujemne
    (10, -2, 8),        # Liczba dodatnia i ujemna
    (5, 0, 5)           # Liczba i zero
])
def test_dodawania_wielu_przypadkow(a, b, oczekiwany_wynik):
    assert dodaj(a, b) == oczekiwany_wynik

# --- Testy dzielenia z poprzedniego zadania (mogą zostać) ---

def test_dzielenia_przez_zero():
    with pytest.raises(ValueError):
        dziel(10, 0)

def test_poprawnego_dzielenia():
    assert dziel(10, 2) == 5