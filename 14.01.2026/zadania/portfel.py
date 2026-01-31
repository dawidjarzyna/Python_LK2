# class NiewystarczajaceSrodki(Exception):
#     """Wyjątek rzucany, gdy brakuje środków w portfelu."""
#     pass

# class Portfel:
#     def __init__(self, saldo_poczatkowe=0):
#         self.saldo = saldo_poczatkowe

#     def wplac(self, kwota):
#         self.saldo += kwota

#     def wydaj(self, kwota):
#         if kwota > self.saldo:
#             raise NiewystarczajaceSrodki("Nie masz tyle pieniędzy!")
#         self.saldo -= kwota

# portfel.py

class NiewystarczajaceSrodki(Exception):
    """Wyjątek rzucany, gdy brakuje środków w portfelu."""
    pass

class Portfel:
    # saldo_poczatkowe ma domyślną wartość 0, ale jeśli coś podamy, musi być liczbą
    def __init__(self, saldo_poczatkowe: float = 0) -> None:
        self.saldo: float = saldo_poczatkowe

    def wplac(self, kwota: float) -> None:
        self.saldo += kwota

    def wydaj(self, kwota: float) -> None:
        if kwota > self.saldo:
            raise NiewystarczajaceSrodki("Nie masz tyle pieniędzy!")
        self.saldo -= kwota