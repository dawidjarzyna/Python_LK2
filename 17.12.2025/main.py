# zad 1
from pathlib import Path
import datetime

base_dir = Path("raporty_dzienne")

dzisiejsza_data = str(datetime.date.today())
sciezka_pliku = base_dir / dzisiejsza_data / "raport.txt"

sciezka_pliku.parent.mkdir(parents=True, exist_ok=True)

tresc = "To jest treść raportu wygenerowana automatycznie."
sciezka_pliku.write_text(tresc, encoding="utf-8")

# f. Wczytaj zawartość pliku z powrotem i wyświetl ją
odczytana_tresc = sciezka_pliku.read_text(encoding="utf-8")
print(f"Zawartość pliku:\n{odczytana_tresc}\n")

# g. Wyświetlenie atrybutów obiektu Path
print("Informacje o ścieżce:")
print(f"Pełna ścieżka: {sciezka_pliku.resolve()}")
print(f"Nazwa pliku: {sciezka_pliku.name}")
print(f"Rozszerzenie: {sciezka_pliku.suffix}")
print(f"Folder nadrzędny: {sciezka_pliku.parent}")

# ------------ zad 2 ----------------
import pickle 

class StanGry:
    def __init__(self, nazwa_gracza, punkty, ekwipunek):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return (f"StanGry(gracz: {self.nazwa_gracza}, ",
                f"punkty: {self.punkty}, ",
                f"eq: {self.ekwipunek}" )

moj_stan = StanGry("Wiedźmin", 1500, ["Miecz", "Mikstura", "Mapa"])

print("Zapisuję stan gry...")
with open("stan_gry.pkl", "wb") as f:
    pickle.dump(moj_stan, f)

print("Odczytuję stan gry z pliku...")
with open("stan_gry.pkl", "rb") as f:
    wczytany_stan = pickle.load(f)

print("-" * 30)
print(f"Wczytany obiekt: {wczytany_stan}")
print(f"Typ obiektu: {type(wczytany_stan)}")
print("-" * 30)

if wczytany_stan.nazwa_gracza == "Wiedźmin":
    print("Sukces! Dane zostały poprawnie odzyskane.")


# ------------ zad 3 ----------------
import csv

def wczytaj_pracownikow(sciezka_pliku: str) -> list:
    lista_pracownikow = []
    
    try:
        with open(sciezka_pliku, mode="r", newline="", encoding="utf-8") as f:
            czytnik = csv.DictReader(f)
            
            for wiersz in czytnik:
                try:
                    wiersz['pensja'] = int(wiersz['pensja'])
                    lista_pracownikow.append(wiersz)
                except ValueError:
                    print(f"Ostrzeżenie: pominięto {wiersz['imie']}")
                    
    except FileNotFoundError:
        print("Błąd: Brak pliku")
    
    return lista_pracownikow

# Przykład użycia:
wynik = wczytaj_pracownikow("pracownicy.csv")
print(wynik)

# ------------ zad 4 ----------------

import csv

def zapisz_raport_sprzedazy(sciezka_pliku: str, dane: list):
    if not dane:
        print("Lista dane jest pusta.")
        return

    pola = list(dane[0].keys())

    with open(sciezka_pliku, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=pola)
        writer.writeheader()
        writer.writerows(dane)

sprzedaz = [
    {"produkt": "Monitor", "sprzedana_ilosc": 10, "przychody": 12000},
    {"produkt": "Myszka", "sprzedana_ilosc": 50, "przychody": 2500},
    {"produkt": "Klawiatura", "sprzedana_ilosc": 30, "przychody": 4500}
]

zapisz_raport_sprzedazy("raport.csv", sprzedaz)

try:
    with open("raport.csv", "r", encoding="utf-8") as sprawdz:
        print(sprawdz.read())
except FileNotFoundError:
    print("Plik nie został utworzony.")

# ------------ zad 5 ----------------
# do tego plik konfigruacja.json
import json

def wczytaj_konfiguracje(sciezka_pliku: str) -> dict:
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

dane = wczytaj_konfiguracje("konfiguracja.json")

if dane:
    print(dane['baza_danych']['uzytkownik'])
else:
    print("Błąd wczytywania danych.")

# ------------ zad 6 ----------------
import json

def zapisz_jako_json(dane: dict | list, sciezka_pliku: str):
    try:
        with open(sciezka_pliku, "w", encoding="utf-8") as f:
            json.dump(
                dane, 
                f, 
                indent=4, 
                ensure_ascii=False #Kluczowe dla polskich znaków!
            )
        print("Sukces: Plik został zapisany.")
    except OSError:
        print("Błąd: Nie udało się zapisać pliku.")

moje_dane = {
    "uzytkownik": "gżegżółka",
    "id": 123,
    "ulubiony_kolor": "żółty",
    "miasto": "Łódź"
}

zapisz_jako_json(moje_dane, "dane.json")

try:
    with open("dane.json", "r", encoding="utf-8") as sprawdz:
        print(sprawdz.read())
except FileNotFoundError:
    print("Plik nie istnieje.")

# ------------ zad 7 ----------------
import json
from pydantic import BaseModel, ValidationError

class SpecyfikacjaModel(BaseModel):
    procesor: str
    ram_gb: int

class ProduktModel(BaseModel):
    nazwa_produktu: str
    id_produktu: str
    cena: float
    dostepny: bool
    tagi: list[str]
    specyfikacja: SpecyfikacjaModel

def przygotuj_plik_produkt():
    tresc = {
        "nazwa_produktu": "Smartfon XYZ",
        "id_produktu": "prod-12345",
        "cena": "1999.99",
        "dostepny": True,
        "tagi": ["elektronika", "nowość"],
        "specyfikacja": {
            "procesor": "SuperChip 1000",
            "ram_gb": 8
        }
    }
    with open("produkt.json", "w", encoding="utf-8") as f:
        json.dump(tresc, f, indent=4)

def wczytaj_i_waliduj_produkt(sciezka: str) -> ProduktModel | None:
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            dane_json = json.load(f)
            return ProduktModel.model_validate(dane_json)
    except FileNotFoundError:
        print("Błąd: Plik nie istnieje.")
    except json.JSONDecodeError:
        print("Błąd: Niepoprawny format JSON.")
    except ValidationError as e:
        print(f"Błąd walidacji danych: {e}")
    return None

przygotuj_plik_produkt()

produkt = wczytaj_i_waliduj_produkt("produkt.json")

if produkt:
    print(f"Produkt: {produkt.nazwa_produktu}")
    print(f"Procesor: {produkt.specyfikacja.procesor}")
    print(f"Cena: {produkt.cena} PLN")

# ------------ zad 8 ----------------
import io,csv

def generuj_raport_csv_w_pamięci(dane: list[dict]) -> io.StringIO:
    plik_w_pamieci = io.StringIO()
    
    if dane:
        pola = list(dane[0].keys())
        writer = csv.DictWriter(plik_w_pamieci, fieldnames=pola)
        writer.writeheader()
        writer.writerows(dane)
    
    plik_w_pamieci.seek(0)
    return plik_w_pamieci

def przetworz_raport(plik):
    print(plik.read())

dane_sprzedazy = [
    {"produkt": "Laptop", "ilosc": 5, "cena": 4500},
    {"produkt": "Monitor", "ilosc": 10, "cena": 1200},
    {"produkt": "Mysz", "ilosc": 20, "cena": 150}
]

raport_ram = generuj_raport_csv_w_pamięci(dane_sprzedazy)
przetworz_raport(raport_ram)

# ------------ zad 9 ----------------
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='parser.log',
    filemode='w',
    encoding='utf-8'
)

linie_do_przetworzenia = [
    "INFO: Uruchomiono system.",
    "DEBUG: Sprawdzam status.",
    "WARNING: Niski poziom baterii.",
    "ERROR: Nie można połączyć z serwerem."
]

def przetworz_logi(linie: list):
    for linia in linie:
        if linia.startswith("INFO:"):
            logging.info(linia[5:].strip())
        elif linia.startswith("DEBUG:"):
            logging.debug(linia[6:].strip())
        elif linia.startswith("WARNING:"):
            logging.warning(linia[8:].strip())
        elif linia.startswith("ERROR:"):
            logging.error(linia[6:].strip())
        else:
            logging.warning(f"Nierozpoznwalna linia: {linia}")

przetworz_logi(linie_do_przetworzenia)

try:
    with open("parser.log", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Plik logów nie został utworzony.")
