# #zadanie 1
plik = open("dziennik.txt", "w")

plik.write("Pierwszy wpis.\n")
plik.write("Wszystko działa.\n")

plik.close()

print("Plik 'dziennik.txt' został utworzony i zapisany.")
print("-" * 30)


# --- Część b: ---


print(">>> KROK C: Odczyt zawartości pliku...")

plik = open("dziennik.txt", "r")

zawartosc = plik.read()


print("Zawartość pliku:")
print(zawartosc)


plik.close()
print("-" * 30)


# --- Część d: Dopisywanie (Append) ---
print(">>> KROK D: Dopisywanie nowej linii...")

plik = open("dziennik.txt", "a")
plik.write("Dodaję kolejną linię.\n")

# 3. Zamknij plik
plik.close()

plik = open("dziennik.txt", "r")
calkowita_tresc = plik.read()
print("Całkowita zawartość po dopisaniu:")
print(calkowita_tresc)
plik.close()

#----------------------------------
#zadanie 2
import datetime
def oblicz_rok_urodzenia(sciezka_pliku):
    plik = None
    try:
       plik = open(f'{sciezka_pliku}','r')
       zawartosc = plik.read()
       wiek = int(zawartosc.strip())
       rok_urodzenia = datetime.date.today().year - wiek
       print(rok_urodzenia)
    except FileNotFoundError:
        print("BŁĄD: Nie znaleziono pliku!")
    except ValueError:
        print("BŁĄD: Zawartość pliku nie jest poprawną liczbą!")
    finally:
        if plik:
            plik.close()
            print("Plik został zamknięty.")
oblicz_rok_urodzenia('wiek.txt')
#----------------------------------------------------------------
#zadanie 3
filename = "dziennik_with.txt"
with open(filename, "w", encoding="utf-8") as plik:
    plik.write("Pierwszy wpis przy użyciu with.\n")
    
print("Zapis zakończony.\n")


print(">>> KROK B: Odczyt zawartości...")

with open(filename, "r", encoding="utf-8") as plik:
    zawartosc = plik.read()
    print("Aktualna zawartość pliku:")
    print(zawartosc)


print(">>> KROK C: Dopisywanie nowej linii...")

with open(filename, "a", encoding="utf-8") as plik:
    plik.write("To jest linia dopisana w trybie append.\n")

print("Dopisano nową linię.\n")


print(">>> KROK D: Weryfikacja końcowa...")

with open(filename, "r", encoding="utf-8") as plik:
    ostateczna_tresc = plik.read()
    print("Ostateczna zawartość pliku:")
    print(ostateczna_tresc)
#----------------------------------------------------------------
# #zadanie 4
class NiepoprawnaIloscProduktuError(ValueError):
    def dodaj_do_koszyka(produkt,ilosc):
            if not isinstance(ilosc,int) and ilosc <= 0:
                raise NiepoprawnaIloscProduktuError("Ilość produktów musi być dodatnia!")
            else:
                print(f"Dodano nowy produkt!\nPrzedmiot: {produkt},\nilość: {ilosc}")
    try:
        dodaj_do_koszyka('mleko',5)
        dodaj_do_koszyka('maslo',10)
    except NiepoprawnaIloscProduktuError as e:
        print(f"Wystąpił błąd logiki biznesowej! {e}")
#----------------------------------------------------------------
#zadanie 5
import time
class MiernikCzasu():
    def __init__(self):
        self.czas_trwania = 0

    def __enter__(self):
        print("Rozpoczynam pomiar.")
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.koniec = time.perf_counter()

        czas_trwania = self.koniec - self.start
        print(f"Koniec. Czas trwania operacji: {czas_trwania:.6f} sekundy.")

print(">>> Testowanie Miernika Czasu...")


with MiernikCzasu():
    suma = sum(n for n in range(10_000_000))
    print(f"Obliczona suma: {suma}")

print(">>> Program zakończony.")
#----------------------------------------------------------------
#zadanie 6 (Bezpieczny zapis)
import os

class BezpiecznyZapis:
    def __init__(self, sciezka):
        self.sciezka_docelowa = sciezka
        self.sciezka_tymczasowa = sciezka + ".tmp"

    def __enter__(self):
        self.plik = open(self.sciezka_tymczasowa, "w", encoding="utf-8")
        return self.plik

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        self.plik.close()

        if typ_bledu is None:
            if os.path.exists(self.sciezka_docelowa):
                os.remove(self.sciezka_docelowa)
            os.rename(self.sciezka_tymczasowa, self.sciezka_docelowa)
        else:
            if os.path.exists(self.sciezka_tymczasowa):
                os.remove(self.sciezka_tymczasowa)

nazwa_pliku = "konfiguracja.txt"

with open(nazwa_pliku, "w", encoding="utf-8") as f:
    f.write("Stara konfiguracja.")

print("Przed zmianami:")
with open(nazwa_pliku, "r", encoding="utf-8") as f:
    print(f.read())

with BezpiecznyZapis(nazwa_pliku) as f:
    f.write("Nowa konfiguracja.")

print("Po udanym zapisie:")
with open(nazwa_pliku, "r", encoding="utf-8") as f:
    print(f.read())

try:
    with BezpiecznyZapis(nazwa_pliku) as f:
        f.write("Te dane nie powinny zostac zapisane.")
        raise RuntimeError("Wystapil blad")
except RuntimeError:
    print("Wystapil oczekiwany blad.")

print("Po bledzie (plik powinien pozostac bez zmian):")
with open(nazwa_pliku, "r", encoding="utf-8") as f:
    print(f.read())

# --- Zadanie 7: Praktyczny Parser Logów ---

def zlicz_bledy(sciezka_pliku):
    """
    Funkcja zlicza wystąpienia logów o poziomie ERROR w podanym pliku.
    Obsługuje błędy formatu linii oraz brak pliku.
    """
    liczba_bledow = 0
    
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as plik:
            for linia in plik:
                linia = linia.strip() 
                if not linia:  
                    continue
                try:
                    poziom, wiadomosc = linia.split(':', 1)
                    if poziom == "ERROR":
                        liczba_bledow += 1
                        
                except ValueError:
                    continue
                    
    except FileNotFoundError:
        return 0

    return liczba_bledow

nazwa_loga = "log.txt"
with open(nazwa_loga, "w", encoding="utf-8") as f:
    f.write("INFO:Uruchomiono serwer.\n")
    f.write("DEBUG:Nawiązano połączenie z bazą.\n")
    f.write("ERROR:Nie udało się przetworzyć żądania #123.\n") # Błąd 1
    f.write("To jest błędna linia bez dwukropka\n")            # Zła linia (powinna być zignorowana)
    f.write("INFO:Zakończono zadanie.\n")
    f.write("ERROR:Błąd autoryzacji użytkownika 'admin'.\n")    # Błąd 2

print(">>> TEST 1: Plik poprawny z błędami")
wynik = zlicz_bledy(nazwa_loga)
print(f"Liczba znalezionych błędów ERROR: {wynik}") # Oczekiwane: 2

print("\n>>> TEST 2: Plik nieistniejący")
wynik_brak = zlicz_bledy("nieistnieje.txt")
print(f"Wynik dla braku pliku: {wynik_brak}") # Oczekiwane: 0

#zadanie 8
class IgnorujBledy:
    def __init__(self, bledy_do_ignorowania):
        self.bledy_do_ignorowania = bledy_do_ignorowania

    def __enter__(self):
        pass

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if typ_bledu is not None:
            if issubclass(typ_bledu, self.bledy_do_ignorowania):
                print(f"Zignorowano błąd: {wart_bledu}")
                return True
        return False

print("TEST 1: Ignorowanie ValueError")
with IgnorujBledy((ValueError, TypeError)):
    print("Przed błędem")
    int("abc")
    print("Ta linia się nie wykona")
print("Po bloku with - program działa dalej")
print("\nTEST 2: Przepuszczenie ZeroDivisionError")
try:
    with IgnorujBledy((ValueError, TypeError)):
        1 / 0
except ZeroDivisionError:
    print("Złapano ZeroDivisionError - prawidłowo, bo nie był ignorowany.")


#zadanie 9

def podmien_imie(sciezka, nowe_imie):
    with open(sciezka, "r+", encoding="utf-8") as plik:
        tresc = plik.read()
        nowa_tresc = tresc.replace("[IMIE]", nowe_imie)

        plik.seek(0)
        plik.write(nowa_tresc)


sciezka = "szablon.txt"

with open(sciezka, "w", encoding="utf-8") as f:
    f.write("Witaj, [IMIE]!")

podmien_imie(sciezka, "Anna")


print("TEST 1 (Anna - krótsze):")
with open(sciezka, "r", encoding="utf-8") as f:
    print(f"Zawartość pliku: '{f.read()}'")
print("-" * 20)

with open(sciezka, "w", encoding="utf-8") as f:
    f.write("Witaj, [IMIE]!")

podmien_imie(sciezka, "Krzysztof")

print("TEST 2 (Krzysztof - dłuższe):")
with open(sciezka, "r", encoding="utf-8") as f:
    print(f"Zawartość pliku: '{f.read()}'")