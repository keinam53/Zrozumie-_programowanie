# collection = ["ciastko", "książka", "jabłko"]
# for element in collection:
#     print(element)

# favourite_sports = ["Pływanie", "Siłownia", "Bieg", "koszykówka"]
# for sports in favourite_sports:
#     print(sports)

# kod = input("Podaj kod pocztowy ")
# for i in kod:
#     print(i)

# expenditures = {
#     "prąd": 250,
#     "woda": 30.45,
#     "zakupy": [
#         120.15,
#         170.53,
#         20.15
#     ]
# }
# for expenditures_name in expenditures:
#     # print(expenditures_name)
#     print(f"{expenditures_name} - {expenditures[expenditures_name]}")
# for wartosci in expenditures.values():
#     print(wartosci)
# for expenditures_name, wartosc in expenditures.items():
#     print(f"{expenditures_name} - {wartosc}")

#Krotkę można "rozpakować"
# item = ("prąd", 360)
# name, value = item
# print(name, value)

# post_code = input("Podaj kod pocztowy ")
# for index, letter in enumerate(post_code):
#     print(f"{[index]} - {letter}")

# favourite_sports = ["Pływanie","Siłownia","Bieg","koszykówka"]
# for index, sports in enumerate(favourite_sports):
#     if index % 2 == 0:
#         print(sports)

#ZAD1
grades = []
oceny_input = input("Podaj ocenę, jeśli skończyłeś naciśnij X: ")
while oceny_input != "X":
    ocena = int(oceny_input)
    grades.append(ocena)
    oceny_input = input("Podaj ocenę, jeśli skończyłeś naciśnij X: ")

suma = 0
for ocena in grades:
    suma = suma + ocena
# suma = sum(grades)
srednia = suma / len(grades)
print(suma)
print(f"Twoja średnia wynosi {srednia:.2f}")

#ZAD2
# numer = input("Podaj swój nr.tel ")
# numer = numer.replace("-","")
# nr_sformatowany = ""
# for index, liczba in enumerate(numer):
#     if index % 3 == 0 and index != 0:
#         nr_sformatowany += "-"
#     nr_sformatowany += numer[index]
# print(nr_sformatowany)

#ZAD3
print("Kalkulator miesięcznych wydatków")
wydatki = {}
nazwa_kategorii = input("Podaj nazwę kategorii albo zakończ wpisując X ")
while nazwa_kategorii != "X":
    wydatki[nazwa_kategorii] = []
    wydatek = input(f"Dodaj wydatek do kategorii {nazwa_kategorii} lub zakończ X ")
    while wydatek != "X":
        wydatek_wartosc = float(wydatek)
        wydatki[nazwa_kategorii].append(wydatek_wartosc)
        wydatek = input(f"Dodaj wydatek do kategorii {nazwa_kategorii} lub zakończ X ")
    nazwa_kategorii = input("Podaj nazwę kategorii albo zakończ wpisując X ")
suma_wydatkow = 0
for kategorie_wydatkow in wydatki.values():
    for wydatki_wartosc in kategorie_wydatkow:
        suma_wydatkow = suma_wydatkow + wydatki_wartosc
wydatki_procent = {}
for nazwa_kategorii, kategorie_wydatkow in wydatki.items():
    suma_kategorii = 0
    suma_kategorii = sum(kategorie_wydatkow)
    wydatki_procent[nazwa_kategorii] = suma_kategorii * 100 / suma_wydatkow
najwazniejsza_kategoria = None
najwazniejsza_kategoria_procent = 0
for category, procent in wydatki_procent.items():
    if procent > najwazniejsza_kategoria_procent:
        najwazniejsza_kategoria_procent = procent
        najwazniejsza_kategoria = nazwa_kategorii
if najwazniejsza_kategoria is not None:
    print(f"Najwięcej wydajesz na {nazwa_kategorii} = {najwazniejsza_kategoria_procent:.2f}% wszystkich wydatków")
for category, procent in wydatki_procent.items():
    print(f"Na {category} wydajesz {procent:.2f}% miesięcznych wydatków")


