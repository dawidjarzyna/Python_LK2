# ------------ zad 1 ---------------
class WlasnyRangeIterator:
    def __init__(self, wlasny_range_obj):
        self.wlasny_range_obj = wlasny_range_obj
        self.biezaca_wartosc = wlasny_range_obj.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.biezaca_wartosc < self.wlasny_range_obj.stop:
            wynik = self.biezaca_wartosc
            self.biezaca_wartosc += 1
            return wynik
        else:
            raise StopIteration

class WlasnyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return WlasnyRangeIterator(self)


moj_zakres = WlasnyRange(2, 5)
for liczba in moj_zakres:
    print(liczba)

#------------ zad 2 ----------------
class WlasnyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        biezaca_wartosc = self.start
        while biezaca_wartosc < self.stop:
            yield biezaca_wartosc
            biezaca_wartosc += 1


moj_zakres = WlasnyRange(2, 5)
for liczba in moj_zakres:
    print(liczba)

#------------- zad 3 ---------------
import csv
from pathlib import Path

def czytaj_duzy_csv(sciezka_pliku: str | Path):
    with open(sciezka_pliku, 'r', encoding='utf-8') as plik:
        
        reader = csv.DictReader(plik)
        
        for wiersz in reader:
            wiersz['wiek'] = int(wiersz['wiek'])
            yield wiersz


print("\n--- Zadanie 3: Osoby powyżej 40 roku życia ---")
    
for osoba in czytaj_duzy_csv('dane.csv'):
    if osoba['wiek'] > 40:
        print(f"{osoba['imie']} {osoba['nazwisko']}, wiek: {osoba['wiek']}")

#-------------- zad 4 ----------------
import csv
from pathlib import Path


def czytaj_duzy_csv(sciezka_pliku: str | Path):
    with open(sciezka_pliku, mode='r', encoding='utf-8') as plik:
        reader = csv.DictReader(plik)
        for wiersz in reader:
            wiersz['wiek'] = int(wiersz['wiek'])
            yield wiersz

zrodlo = czytaj_duzy_csv('dane.csv')

osoby_po_30 = (osoba for osoba in zrodlo if osoba['wiek'] > 30)

opisy = (f"{o['imie']} {o['nazwisko']}".upper() for o in osoby_po_30)

for opis in opisy:
    print(opis)

#--------------- zad 5 -----------------
import csv
import itertools  # Niezbędne do groupby
from pathlib import Path


def czytaj_duzy_csv(sciezka_pliku: str | Path):
    with open(sciezka_pliku, mode='r', encoding='utf-8') as plik:
        reader = csv.DictReader(plik)
        for wiersz in reader:
            wiersz['wiek'] = int(wiersz['wiek'])
            yield wiersz

if __name__ == "__main__":

    generator = czytaj_duzy_csv('dane.csv')
    lista_osob = list(generator)

    def klucz_funkcja(osoba):
        return osoba['nazwisko'][0]

    lista_osob.sort(key=klucz_funkcja)

    grupowanie = itertools.groupby(lista_osob, key=klucz_funkcja)

    for litera, grupa in grupowanie:
        osoby_w_grupie = list(grupa)
        
        suma_wieku = sum(o['wiek'] for o in osoby_w_grupie)
        ilosc_osob = len(osoby_w_grupie)
        
        srednia = suma_wieku / ilosc_osob
        
        print(f"Litera '{litera}': {ilosc_osob} osób, Średni wiek: {srednia:.1f}")

# -------------- zad 6 -------------------
import csv
import itertools
from pathlib import Path

def czytaj_duzy_csv(sciezka_pliku: str | Path):
    with open(sciezka_pliku, mode='r', encoding='utf-8') as plik:
        reader = csv.DictReader(plik)
        for wiersz in reader:
            wiersz['wiek'] = int(wiersz['wiek'])
            yield wiersz

print("--- Zadanie 6: Rozdzielanie strumieni (tee) ---\n")


zrodlo = czytaj_duzy_csv('dane.csv')

iter_analiza1, iter_analiza2 = itertools.tee(zrodlo, 2)

def dlugosc_imienia_nazwiska(osoba):
    return len(osoba['imie'] + osoba['nazwisko'])

najdluzszy = max(iter_analiza1, key=dlugosc_imienia_nazwiska)

liczba_osob = 0
laczny_wiek = 0

for osoba in iter_analiza2:
    liczba_osob += 1
    laczny_wiek += osoba['wiek']

print(f"Analiza 1 (Max długość): {najdluzszy['imie']} {najdluzszy['nazwisko']}")
print(f"Analiza 2 (Statystyki): Razem osób: {liczba_osob}, Łączny wiek: {laczny_wiek}")

#-------------- zad 7 --------------------
import itertools

# --- KROK WSTĘPNY: Tworzymy plik logs.txt ---
logs_content = """1.2.3.4 - - [11/Nov/2023] "GET /" 200 1500
5.6.7.8 - - [11/Nov/2023] "GET /admin" 401 100
1.2.3.4 - - [11/Nov/2023] "POST /login" 404 250
9.1.2.3 - - [11/Nov/2023] "GET /" 200 1800
5.6.7.8 - - [11/Nov/2023] "GET /data.json" 200 9500
1.2.3.4 - - [11/Nov/2023] "GET /static/img.jpg" 404 50
2.3.4.5 - - [11/Nov/2023] "GET /api/v1/users" 403 120"""

with open('logs.txt', 'w', encoding='utf-8') as f:
    f.write(logs_content)

def czytaj_logi(sciezka):
    with open(sciezka, 'r', encoding='utf-8') as f:
        for line in f:
            yield line

logi_stream = czytaj_logi('logs.txt')

parsed_stream = (line.split() for line in logi_stream)

bledy_klienta = (
    parts for parts in parsed_stream 
    if 400 <= int(parts[-2]) < 500
)

dane_ip_rozmiar = (
    (parts[0], int(parts[-1])) 
    for parts in bledy_klienta
)

posortowane_dane = sorted(dane_ip_rozmiar, key=lambda x: x[0])

grupowanie = itertools.groupby(posortowane_dane, key=lambda x: x[0])

wyniki_agregacji = []
for ip, grupa in grupowanie:
    suma_bajtow = sum(rekord[1] for rekord in grupa)
    wyniki_agregacji.append((ip, suma_bajtow))

top_3_adresy = sorted(wyniki_agregacji, key=lambda x: x[1], reverse=True)[:3]

print("Top 3 adresy IP generujące błędy 4xx (wg sumy danych):")
for ip, ruch in top_3_adresy:
    print(f"IP: {ip}, Ruch: {ruch} bajtów")

# -------------- zad 8 ------------------
def monitor_temperatury(prog_alarmowy):
    suma = 0
    licznik = 0
    srednia = 0.0

    try:
        while True:
            odczyt = yield srednia

            if odczyt is None:
                suma = 0
                licznik = 0
                srednia = 0.0
            else:
                suma += odczyt
                licznik += 1
                srednia = suma / licznik

                if srednia > prog_alarmowy:
                    print(f"!!! ALARM! Średnia {srednia:.2f} przekroczyła próg {prog_alarmowy} !!!")

    finally:
        print("Czujnik wyłączony.")


czujnik = monitor_temperatury(25.0)

next(czujnik)

print(czujnik.send(20))
print(czujnik.send(30))
print(czujnik.send(40))
print(czujnik.send(None))
print(czujnik.send(10))

czujnik.close()