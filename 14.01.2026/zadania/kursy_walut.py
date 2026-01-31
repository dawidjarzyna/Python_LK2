# kursy_walut.py
import requests

def pobierz_cene_euro():
    # Adres API Narodowego Banku Polskiego
    url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/"
    
    # Wykonujemy prawdziwe zapytanie do sieci
    response = requests.get(url)
    
    # Zamieniamy odpowiedź na słownik (JSON)
    dane = response.json()
    
    # Wyciągamy kurs średni (mid) ze struktury JSON NBP
    return dane['rates'][0]['mid']