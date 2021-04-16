# wydaki = [120, 300, 250.45, 300, 40, 500]
# for ceny in wydaki:
#     print(ceny)
#     if ceny > 1000:
#         print("Znaleziono drogi wydatek ")
#         break
# else:
#     print("Nie znaleziono nic drogieg")

# grades = []
# while True:
#     oceny_input = input("Podaj ocenę, jeśli skończyłeś naciśnij X: ")
#     if oceny_input == "X":
#         break
#     ocena = int(oceny_input)
#     grades.append(ocena)
# suma = sum(grades)
# srednia = suma / len(grades)
# print(suma)
# print(f"Twoja średnia wynosi {srednia:.2f}")

# grades = []
# while len(grades) < 5:
#     oceny_input = input("Podaj ocenę, jeśli skończyłeś naciśnij X: ")
#     if oceny_input == "X":
#         break
#     ocena = int(oceny_input)
#     grades.append(ocena)
# else:
#     print("Wystarczy")
#
# suma = sum(grades)
# srednia = suma / len(grades)
# print(suma)
# print(f"Twoja średnia wynosi {srednia:.2f}")

# favourite_sports = ["Pływanie","Siłownia","Bieg","koszykówka"]
# for index, sports in enumerate(favourite_sports):
#     if index % 2 != 0:
#         continue
#     print(sports)

#ZAD1
# przedmioty = ["matematyka", "fizyka", "biologia", "chemia"]
# oceny = []
# for przedmiot in przedmioty:
#     ocena = int(input(f"Podaj ocenę z przedmiotu: {przedmiot} "))
#     oceny.append(ocena)
# for ocena in oceny:
#     if ocena == 1:
#         print("Nie zdajesz")
#         break
# else:
#     print("Zdajesz")

#ZAD2
# print("Kalkulator miesięcznych wydatków")
# wydatki = {}
# while True:
#     nazwa_kategorii = input("Podaj kategorię wydatków lub zakończ X ")
#     if nazwa_kategorii == "X":
#         break
#     wydatki[nazwa_kategorii] = []
#     while True:
#         wydatek = input(f"Podaj kwotę wydatków z kategorii: {nazwa_kategorii} lub zakończ X ")
#         if wydatek == "X":
#             break

#ZAD3
lista = []
liczby_input = input("Podaj liczbę lub zakończ X ")
while liczby_input != "X":
    liczba = int(liczby_input)
    lista.append(liczba)
    liczby_input = input("Podaj liczbę lub zakończ X ")
for liczba in lista:
    if liczba %2 == 0:
        continue
    print(f"Liczba nieparzysta: {liczba}")


