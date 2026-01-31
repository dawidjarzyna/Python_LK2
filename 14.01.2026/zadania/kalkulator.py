# ---- Zad 1 ----
def dodaj(a, b):
    return a + b

def dziel(a, b):
    if b == 0:
        # Zgodnie z zadaniem, rzucamy ValueError przy dzieleniu przez zero
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

# ---- Zad 2, zad 6 ----
# Przyjmujemy liczby (float), zwracamy liczbę (float)
def dodaj(a: float, b: float) -> float:
    return a + b

def dziel(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

# ---- Zad 8 ----
def srednia(liczby: list[float]) -> float | None:
    if not liczby:  # Sprawdzamy, czy lista jest pusta
        return None
    return sum(liczby) / len(liczby)

#---- Zad 9 ----
from kalkulator import srednia

def test_srednia_trzy_liczby():
    # Przypadek listy z liczbami
    assert srednia([1, 2, 3]) == 2.0

def test_srednia_pusta():
    # Przypadek pustej listy (powinno zwrócić None)
    assert srednia([]) is None