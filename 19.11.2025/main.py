# zad 2
# class Gracz():
#     def __init__(self,imie,hp): #konstruktor
#         self.imie = imie
#         self.hp = hp

#     def pokaz_status(self): #metoda
#         print(f"Gracz: {self.imie} HP: {self.hp}")

#     def otrzymaj_obraznia(self, ilosc):
#         self.hp -= ilosc
#         return f"Zostało Ci HP: {self.hp}"
    
#     def __str__(self):
#         return f"Gracz: {self.imie} HP: {self.hp}"
    
#     def __repr__(self):
#         return f"Gracz(imie={self.imie}, hp={self.hp}) "
        

# gracz = Gracz("Aragom",100)

# gracz.pokaz_status()
# gracz.otrzymaj_obraznia(40)
# print(gracz)

#zad 3
# class Gracz():
#     liczba_graczy = 0
#     def __init__(self,imie,hp): #konstruktor
#         self.imie = imie
#         self.hp = hp
#         Gracz.liczba_graczy += 1 # utworzony poza konstruktorem, aby inkrementować trzeba wywołać poprzez klase

#     def pokaz_status(self): #metoda
#         print(f"Gracz: {self.imie} HP: {self.hp}")

#     def otrzymaj_obraznia(self, ilosc):
#         self.hp -= ilosc
#         return f"Zostało Ci HP: {self.hp}"
    
#     def __str__(self):
#         return f"Gracz: {self.imie} HP: {self.hp}"
    
#     def __repr__(self):
#         return f"Gracz(imie={self.imie}, hp={self.hp}) "
        

# print(Gracz.liczba_graczy)
# gracz = Gracz("Aragom",100)
# gracz2 = Gracz("Ala",50)
# gracz.pokaz_status()
# gracz2.pokaz_status()
# print(Gracz.liczba_graczy)

#zad 4
class Gracz():
    liczba_graczy = 0
    def __init__(self,imie,hp): #konstruktor
        self.imie = imie
        self._hp = hp #_ oznacza że zmienna jest chroniona
        self.ekwipunek = Ekwipunek() #nowa instancja
        
        Gracz.liczba_graczy += 1 # utworzony poza konstruktorem, aby inkrementować trzeba wywołać poprzez klase
        
    @staticmethod
    def sprawdz_poprawnosc_imienia(imie):
        if (isinstance(imie,str) and imie.capitalize()):
            return True
        else:
            return False
    def pokaz_status(self): #metoda
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
        if isinstance(other,Gracz) and other.imie == self.imie:
            return True
        else:
            return False
    
    @property #getter - pobiera wartość
    def hp(self):
        return self._hp
    
    @hp.setter #setter - ustawia
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc
    
class Wojownik(Gracz): #dziedziczenie
    def __init__(self, hp, imie, sila):
        super().__init__(hp, imie)
        self.sila = sila

    def __add__(self, other):
        other.imie += self.imie
        other.hp += self.hp 
        other.sila = self.sila
        return f"- {other.imie},-\n {other.hp},-\n {other.sila}"

    @classmethod
    def stworz_berserkera(cls, imie):
        return cls(imie=imie,hp=80,sila=40)

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f" Moja siła to: {self.sila}")

    def atak(self):
        print(f"{self.imie} atakuje z siłą: {self.sila}")
    
class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jestem {self.mana}")

class Ekwipunek():
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def pokaz_przedmioty(self):
        for rzecz in self.przedmioty:
            print(f"-{rzecz}")

print(Gracz.liczba_graczy)
gracz = Gracz("Aragom",100)
gracz2 = Gracz("Ala",50)
gracz.pokaz_status()
gracz2.pokaz_status()

print(Gracz.liczba_graczy)

wojownik1 = Wojownik("Jan",150,70)
mag1 = Mag("Magillo",200,45)

druzyna = [gracz, wojownik1, mag1]

for user in druzyna:
    user.przedstaw_sie()
    print("-" * 20)

gracz.hp = -50
gracz.przedstaw_sie()

gracz.ekwipunek.dodaj_przedmiot("Miecz")
gracz.ekwipunek.dodaj_przedmiot("Tarcza")

print("\n ---------- Sprawdzenie ekwipunku: ---------- ")
gracz.ekwipunek.pokaz_przedmioty()

#zad 8
berserker = Wojownik.stworz_berserkera("Olaf")
berserker.przedstaw_sie()

print(Gracz.sprawdz_poprawnosc_imienia("Aragon"))

#zad 9
print("------------ zad 9 -----")
gracz_1 = Gracz("Aron",120)
gracz_2 = Gracz("Aron", 150)
print(gracz_1.__eq__(gracz_2))

wojownik_1 = Wojownik(120, "Ala", 100)
wojownik_2 = Wojownik(50, "Baron", 80)

print(wojownik_1.__add__(wojownik_2))

