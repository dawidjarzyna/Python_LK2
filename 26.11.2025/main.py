# class Gracz():
#     liczba_graczy = 0
#     def __init__(self,imie,hp): #konstruktor
#         self.imie = imie
#         self._hp = hp #_ oznacza że zmienna jest chroniona
#         self.ekwipunek = Ekwipunek() #nowa instancja
        
#         Gracz.liczba_graczy += 1 # utworzony poza konstruktorem, aby inkrementować trzeba wywołać poprzez klase
        
#     @staticmethod
#     def sprawdz_poprawnosc_imienia(imie):
#         if (isinstance(imie,str) and imie.capitalize()):
#             return True
#         else:
#             return False
#     def pokaz_status(self): #metoda
#         print(f"Gracz: {self.imie} HP: {self.hp}")

#     def przedstaw_sie(self):
#         print(f"-> Jestem {self.imie} mam hp: {self.hp}")

#     def otrzymaj_obraznia(self, ilosc):
#         self.hp -= ilosc
#         return f"Zostało Ci HP: {self.hp}"
    
#     def __str__(self):
#         return f"Gracz: {self.imie} HP: {self.hp}"
    
#     def __repr__(self):
#         return f"Gracz(imie={self.imie}, hp={self.hp}) "
#     def __eq__(self, other):
#         if isinstance(other,Gracz) and other.imie == self.imie:
#             return True
#         else:
#             return False
        
#     def ___It___(self,other): # ---------------- 3 grudnia 2025 ------------------
#         if not isinstance(other, Gracz):
#             return NotImplemented
#         else:
#             return self.hp < other.hp
         
#     # @property #getter - pobiera wartość
#     # def hp(self):
#     #     return self._hp
    
#     # @hp.setter #setter - ustawia
#     # def hp(self, nowa_wartosc):
#     #     if nowa_wartosc < 0:
#     #         self._hp = 0
#     #     else:
#     #         self._hp = nowa_wartosc
    
# class Wojownik(Gracz): #dziedziczenie
#     def __init__(self, hp, imie, sila):
#         super().__init__(hp, imie)
#         self.sila = sila

#     def __add__(self, other):
#         other.imie += self.imie
#         other.hp += self.hp 
#         other.sila = self.sila
#         return f"- {other.imie},-\n {other.hp},-\n {other.sila}"

#     @classmethod
#     def stworz_berserkera(cls, imie):
#         return cls(imie=imie,hp=80,sila=40)

#     def przedstaw_sie(self):
#         super().przedstaw_sie()
#         print(f" Moja siła to: {self.sila}")

#     def atak(self):
#         print(f"{self.imie} atakuje z siłą: {self.sila}")
    
# class Mag(Gracz):
#     def __init__(self, imie, hp, mana):
#         super().__init__(imie, hp)
#         self.mana = mana

#     def przedstaw_sie(self):
#         super().przedstaw_sie()
#         print(f"Jestem {self.mana}")

# class Ekwipunek():
#     def __init__(self):
#         self.przedmioty = []

#     def dodaj_przedmiot(self, przedmiot):
#         self.przedmioty.append(przedmiot)

#     def pokaz_przedmioty(self):
#         for rzecz in self.przedmioty:
#             print(f"-{rzecz}")

# print(Gracz.liczba_graczy)
# gracz = Gracz("Aragom",100)
# gracz2 = Gracz("Ala",50)
# gracz.pokaz_status()
# gracz2.pokaz_status()

# print(Gracz.liczba_graczy)

# wojownik1 = Wojownik("Jan",150,70)
# mag1 = Mag("Magillo",200,45)

# druzyna = [gracz, wojownik1, mag1]

# for user in druzyna:
#     user.przedstaw_sie()
#     print("-" * 20)

# gracz.hp = -50
# gracz.przedstaw_sie()

# gracz.ekwipunek.dodaj_przedmiot("Miecz")
# gracz.ekwipunek.dodaj_przedmiot("Tarcza")

# print("\n ---------- Sprawdzenie ekwipunku: ---------- ")
# gracz.ekwipunek.pokaz_przedmioty()

# #zad 8
# berserker = Wojownik.stworz_berserkera("Olaf")
# berserker.przedstaw_sie()

# print(Gracz.sprawdz_poprawnosc_imienia("Aragon"))

# #zad 9
# print("------------ zad 9 -----")
# gracz_1 = Gracz("Aron",120)
# gracz_2 = Gracz("Aron", 150)
# print(gracz_1.__eq__(gracz_2))

# wojownik_1 = Wojownik(120, "Ala", 100)
# wojownik_2 = Wojownik(50, "Baron", 80)

# print(wojownik_1.__add__(wojownik_2))

# gracz1 = Gracz("Aragom",100)
# gracz_2 = Gracz("Ala",50)
# gracz_3 = Gracz("Bart",120)
# gracz_4 = Gracz("Olaf", 80)

# lista = [gracz1,gracz_2,gracz_3,gracz_4]
# posortowane = sorted(lista)
# print(posortowane)

# from dataclasses import dataclass
# @dataclass
# class NazwaKlasy:
#     atrybut1: typ
#     atrybut2: typ = wartosc_domyslna


# # --- NOWY ELEMENT: Zadanie 2 (Deskryptor) ---
# class NieujemnaLiczba:
#     def __set_name__(self, owner, name):
#         # b. Zapisuje nazwę atrybutu (np. "sila" lub "mana")
#         self.name = name

#     def __get__(self, instance, owner):
#         # c. Pobiera wartość ze słownika instancji
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.name)

#     def __set__(self, instance, value):
#         # d. Sprawdza czy wartość < 0, jeśli tak ustawia 0
#         if value < 0:
#             print(f"--- Uwaga: Próba ustawienia ujemnej wartości dla '{self.name}'. Zmieniam na 0. ---")
#             instance.__dict__[self.name] = 0
#         else:
#             instance.__dict__[self.name] = value


# class Gracz:
#     liczba_graczy = 0

#     def __init__(self, imie, hp):
#         self.imie = imie
#         self._hp = hp
#         self.ekwipunek = Ekwipunek()
#         Gracz.liczba_graczy += 1

#     @staticmethod
#     def sprawdz_poprawnosc_imienia(imie):
#         if isinstance(imie, str) and imie.capitalize():
#             return True
#         else:
#             return False

#     def pokaz_status(self):
#         print(f"Gracz: {self.imie} HP: {self.hp}")

#     def przedstaw_sie(self):
#         print(f"-> Jestem {self.imie} mam hp: {self.hp}")

#     def otrzymaj_obraznia(self, ilosc):
#         self.hp -= ilosc
#         return f"Zostało Ci HP: {self.hp}"

#     def __str__(self):
#         return f"Gracz: {self.imie} HP: {self.hp}"

#     def __repr__(self):
#         return f"Gracz(imie={self.imie}, hp={self.hp}) "

#     def __eq__(self, other):
#         if isinstance(other, Gracz) and other.imie == self.imie:
#             return True
#         else:
#             return False

#     def __lt__(self, other):
#         if not isinstance(other, Gracz):
#             return NotImplemented
#         else:
#             return self.hp < other.hp

#     @property
#     def hp(self):
#         return self._hp

#     @hp.setter
#     def hp(self, nowa_wartosc):
#         if nowa_wartosc < 0:
#             self._hp = 0
#         else:
#             self._hp = nowa_wartosc

# class Wojownik(Gracz):
#     # e. Użycie deskryptora zamiast zwykłego atrybutu
#     sila = NieujemnaLiczba()

#     def __init__(self, hp, imie, sila):
#         super().__init__(imie, hp)
#         self.sila = sila  # To wywołuje NieujemnaLiczba.__set__

#     def __add__(self, other):
#         other.imie += self.imie
#         other.hp += self.hp
#         # Obsługa przypadku, gdy other ma atrybut sila (np. jest Wojownikiem)
#         if hasattr(other, 'sila'):
#             other.sila = self.sila
#         return f"- {other.imie},-\n {other.hp},-\n {getattr(other, 'sila', 'Brak siły')}"

#     @classmethod
#     def stworz_berserkera(cls, imie):
#         return cls(imie=imie, hp=80, sila=40)

#     def przedstaw_sie(self):
#         super().przedstaw_sie()
#         print(f" Moja siła to: {self.sila}")

#     def atak(self):
#         print(f"{self.imie} atakuje z siłą: {self.sila}")

# class Mag(Gracz):
#     # e. Użycie deskryptora zamiast zwykłego atrybutu
#     mana = NieujemnaLiczba()

#     def __init__(self, imie, hp, mana):
#         super().__init__(imie, hp)
#         self.mana = mana  # To wywołuje NieujemnaLiczba.__set__

#     def przedstaw_sie(self):
#         super().przedstaw_sie()
#         print(f"Jestem {self.imie}, moja mana to: {self.mana}")

# class Ekwipunek:
#     def __init__(self):
#         self.przedmioty = []

#     def dodaj_przedmiot(self, przedmiot):
#         self.przedmioty.append(przedmiot)

#     def pokaz_przedmioty(self):
#         for rzecz in self.przedmioty:
#             print(f"-{rzecz}")

# # --- Kod Główny / Testy ---

# print(f"Liczba graczy na starcie: {Gracz.liczba_graczy}")
# gracz = Gracz("Aragom", 100)
# gracz2 = Gracz("Ala", 50)
# gracz.pokaz_status()

# wojownik1 = Wojownik(150, "Jan", 70)
# mag1 = Mag("Magillo", 200, 45)

# druzyna = [gracz, wojownik1, mag1]

# for user in druzyna:
#     user.przedstaw_sie()
#     print("-" * 20)

# gracz.hp = -50
# gracz.przedstaw_sie()

# gracz.ekwipunek.dodaj_przedmiot("Miecz")
# gracz.ekwipunek.dodaj_przedmiot("Tarcza")

# print("\n ---------- Sprawdzenie ekwipunku: ---------- ")
# gracz.ekwipunek.pokaz_przedmioty()

# berserker = Wojownik.stworz_berserkera("Olaf")
# berserker.przedstaw_sie()

# print("\n------------ zad 9 (sortowanie i operatory) -----")
# gracz_1 = Gracz("Aron", 120)
# gracz_2 = Gracz("Aron", 150)
# print(f"Czy równi? {gracz_1 == gracz_2}")

# wojownik_1 = Wojownik(120, "Ala", 100)
# wojownik_2 = Wojownik(50, "Baron", 80)
# # print(wojownik_1 + wojownik_2) # Zakomentowane, bo __add__ zwraca stringa, a nie modyfikuje w miejscu w sposób oczywisty dla testów deskryptora

# lista = [Gracz("B", 100), Gracz("A", 50), Gracz("C", 120)]
# posortowane = sorted(lista)
# print(f"Posortowani wg HP: {posortowane}")

# print("\n========== TEST ZADANIE 2: DESKRYPTORY ==========")

# print("1. Tworzę Wojownika z ujemną siłą (-50):")
# zly_wojownik = Wojownik(100, "Słabeusz", -50)
# zly_wojownik.przedstaw_sie() # Powinno pokazać siłę 0

# print("\n2. Tworzę Maga z ujemną maną (-200):")
# zly_mag = Mag("Gargamel", 100, -200)
# zly_mag.przedstaw_sie() # Powinno pokazać manę 0

# print("\n3. Próba zmiany istniejącej siły na ujemną:")
# wojownik1.sila = -999
# print(f"Siła Jana po zmianie na -999: {wojownik1.sila}")

from dataclasses import dataclass
from functools import total_ordering

# --- ZADANIE 4: WŁASNE WYJĄTKI ---
class BrakPunktowZyciaError(Exception):
    pass

# --- ZADANIE 2: DESKRYPTORY ---
class NieujemnaLiczba:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            print(f"--- Uwaga: Próba ustawienia ujemnej wartości dla '{self.name}'. Zmieniam na 0. ---")
            instance.__dict__[self.name] = 0
        else:
            instance.__dict__[self.name] = value

# --- ZADANIE 7: WŁASNE ITERATORY ---
class IteratorEkwipunku:
    def __init__(self, lista_przedmiotow):
        self._przedmioty = lista_przedmiotow
        self._indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indeks < len(self._przedmioty):
            wynik = self._przedmioty[self._indeks]
            self._indeks += 1
            return wynik
        else:
            raise StopIteration

@total_ordering
class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = hp
        self.ekwipunek = Ekwipunek()
        Gracz.liczba_graczy += 1

    @staticmethod
    def sprawdz_poprawnosc_imienia(imie):
        if isinstance(imie, str) and imie.capitalize():
            return True
        else:
            return False

    def pokaz_status(self):
        print(f"Gracz: {self.imie} HP: {self.hp}")

    def przedstaw_sie(self):
        print(f"-> Jestem {self.imie} mam hp: {self.hp}")

    def otrzymaj_obraznia(self, ilosc):
        self.hp -= ilosc
        return f"Zostało Ci HP: {self.hp}"

    def __str__(self):
        return f"Gracz: {self.imie} HP: {self.hp}"

    def __repr__(self):
        return f"Gracz(imie={self.imie}, hp={self.hp}) "

    def __eq__(self, other):
        if isinstance(other, Gracz) and other.imie == self.imie:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Gracz):
            return NotImplemented
        else:
            return self.hp < other.hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc

class Wojownik(Gracz):
    sila = NieujemnaLiczba()

    def __init__(self, hp, imie, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def __add__(self, other):
        other.imie += self.imie
        other.hp += self.hp
        if hasattr(other, 'sila'):
            other.sila = self.sila
        return f"- {other.imie},-\n {other.hp},-\n {getattr(other, 'sila', 'Brak siły')}"

    @classmethod
    def stworz_berserkera(cls, imie):
        return cls(imie=imie, hp=80, sila=40)

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f" Moja siła to: {self.sila}")

    def atakuj(self):
        if self.hp <= 0:
            raise BrakPunktowZyciaError("Postać nie może atakować! (HP = 0)")
        else:
            print(f"{self.imie} wykonuje potężny atak z siłą: {self.sila}!")

    def atak(self):
        print(f"{self.imie} atakuje z siłą: {self.sila}")

class Mag(Gracz):
    mana = NieujemnaLiczba()

    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jestem {self.imie}, moja mana to: {self.mana}")

# --- ZADANIE 6 + 7: EMULACJA KONTENERÓW I ITERATORY ---
class Ekwipunek:
    def __init__(self):
        self._przedmioty = {}

    def __len__(self):
        return len(self._przedmioty)

    def __setitem__(self, klucz, wartosc):
        print(f"[Ekwipunek] Dodano: {klucz} -> {wartosc}")
        self._przedmioty[klucz] = wartosc

    def __getitem__(self, klucz):
        return self._przedmioty[klucz]

    def __delitem__(self, klucz):
        print(f"[Ekwipunek] Usunięto: {klucz}")
        del self._przedmioty[klucz]

    def __repr__(self):
        return f"Ekwipunek(zawartość={self._przedmioty})"

    def __iter__(self):
        return IteratorEkwipunku(list(self._przedmioty.keys()))

    def pokaz_przedmioty(self):
        if not self._przedmioty:
            print("- Pusty ekwipunek")
        for nazwa, opis in self._przedmioty.items():
            print(f"- {nazwa}: {opis}")

# --- ZADANIE 3: DATACLASSES ---
@dataclass
class PunktData:
    x: int
    y: int

# --- ZADANIE 9: OPTYMALIZACJA (__SLOTS__) ---
class PunktLekki:
    # b. Deklaracja slots (rezerwacja miejsca tylko na te atrybuty)
    __slots__ = ('x', 'y')

    # c. Konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y


# --- KOD GŁÓWNY / TESTY ---

print(f"Liczba graczy na starcie: {Gracz.liczba_graczy}")
gracz = Gracz("Aragom", 100)
gracz2 = Gracz("Ala", 50)

wojownik1 = Wojownik(150, "Jan", 70)
mag1 = Mag("Magillo", 200, 45)

print("\n--- Test Deskryptorów ---")
zly_wojownik = Wojownik(100, "Słabeusz", -50)
zly_wojownik.przedstaw_sie() 

print("\n--- Test Wyjątków ---")
try:
    martwy_rycerz = Wojownik(0, "Upadły", 50)
    # martwy_rycerz.atakuj() # Odkomentuj, aby sprawdzić błąd
except BrakPunktowZyciaError as e:
    print(f"Złapano wyjątek: {e}")

print("\n--- Test Total Ordering ---")
print(f"Czy {gracz.hp} > {gracz2.hp}? -> {gracz > gracz2}")

print("\n--- Test Kontenerów i Iteratorów ---")
gracz.ekwipunek["Miecz"] = "Stalowy miecz"
gracz.ekwipunek["Tarcza"] = "Drewniana tarcza"
for przedmiot in gracz.ekwipunek:
    print(f" -> Znalazłem: {przedmiot}")

# --- TEST ZADANIE 9: __SLOTS__ ---
print("\n========== TEST ZADANIE 9: SLOTS ==========")

# 1. Stworzenie instancji
p = PunktLekki(1, 2)
print(f"1. Stworzono punkt lekki: x={p.x}, y={p.y}")

# 2. Próba dodania nowego atrybutu (powinna zakończyć się błędem)
print("2. Próba dodania atrybutu 'z' (oczekiwany AttributeError):")
try:
    p.z = 3
    print("BŁĄD! Udało się dodać atrybut 'z', a nie powinno.")
except AttributeError as e:
    print(f" -> SUKCES! Złapano oczekiwany błąd: {e}")

# 3. Próba odwołania się do __dict__ (powinna zakończyć się błędem)
print("3. Próba odczytu __dict__ (oczekiwany AttributeError):")
try:
    print(p.__dict__)
except AttributeError as e:
    print(f" -> SUKCES! Obiekt nie posiada słownika __dict__: {e}")  