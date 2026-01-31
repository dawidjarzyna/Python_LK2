from kalkulator import srednia

wynik = srednia([])

if wynik is not None:
    print(f"Wynik + 10 to: {wynik + 10}")
else:
    print("Nie można obliczyć średniej - lista była pusta.")