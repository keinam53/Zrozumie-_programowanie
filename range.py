# for a in range(12):
#     print(a)
#
# for a in range(1, 13):
#     print(a)
#
# for a in range(1, 13, 3):
#     print(a)

# print("Kalkulator oprocentowania")
# wartosc_pocz = float(input("Jaką wartość wpłaciłeś? "))
# oprocentowanie = float(input("Jakie jest oprocentowanie? "))
# czas = int(input("Ile lat trwa lokata? "))
# for kazdy_rok in range(1, czas + 1):
#     wartosc_koncowa = wartosc_pocz * (1+oprocentowanie/100)**kazdy_rok
#     print(f"Po {kazdy_rok} roku na lokacie będzie {wartosc_koncowa:.2f} zł")

# sentence = "asadsasadasdaaadajkasdjaks"
# a = sentence.count("s")
# print(a)

#ZAD1
# numer = input("Podaj numer telefonu ")
# for liczby in range(10):
#     liczby_w_numerze = numer.count(str(liczby))
#     print(f"Cyfra {liczby} występuje w numerze {liczby_w_numerze} razy")

#ZAD2
kwota = float(input("Podaj kwotę kredytu "))
oprocentowanie = float(input("Podaj oprocentowanie "))
czas_trwania = int(input("Podaj czas trwania kredytu "))
koszty_pocz = float(input("Podaj koszty początkowe kredytu "))
czas_trwania_mies = czas_trwania * 12
kapital_miesieczny = kwota / (czas_trwania * 12)
laczne_oplaty = koszty_pocz
for miesiac in range(czas_trwania_mies + 1):
    pozostaly_kapital = kwota - (miesiac - 1) * kapital_miesieczny
    rata = (pozostaly_kapital * oprocentowanie / 100) / 12 + kapital_miesieczny
    laczne_oplaty += rata
    print(f"Rata w miesiącu {miesiac} wyniesie {rata:.2f} zł")
print(f"Zaciągając {kwota} zł kredytu na tych warunkach zapłacisz {laczne_oplaty:.2f} zl")


