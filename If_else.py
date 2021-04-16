# name = input("Jak masz na imię? ")
# print("Miło mi Cię poznać", name)
# if len(name) >= 7:
#     print(f"{name} to całkiem długie imię")
# if len(name) < 7:
#     print(f"{name} to krótkie imię")

# age = int(input("Ile masz lat? "))
# if age < 18:
#     print("Nie możesz jeszcze głosować")
# if age >= 18:
#     print("Możesz już głosować")
# if age >= 35:
#     print("Możesz kandydować na prezydenta")

# name = input("Jak masz na imię? ")
# if len(name) >= 7:
#     print(name,"To całkiem długie imię")
# else:
#     print(name,"To krótkie imię")

#zad1
# ceny = []
# price = float(input("Podaj cenę pierwszego produktu "))
# ceny.append(price)
# price = float(input("Podaj cenę drugiego produktu "))
# ceny.append(price)
# price = float(input("Podaj cenę trzeciego produktu "))
# ceny.append(price)
# if ceny[0]>ceny[1]:
#     print("Cena pierwsza jest wyższa od drugiej")
# else:
#     print("Cena pierwsza jest niższa od drugiej")
# if ceny[1]>ceny[2]:
#     print("Cena druga jest wyższa od trzeciej")
# else:
#     print("Cena druga jest niższa od trzeciej")
# if ceny[2]>ceny[0]:
#     print("Cena trzecia jest wyższa od drugiej")
# else:
#     print("Cena trzecia jest niższa od drugiej")

# shopping_list = input("Podaj listę zakupów rozdzielając przecinkiem ")
# shopping_elements = shopping_list.split(",")
# if len(shopping_elements) >= 4:
#     print("Lista zakupów jest długa")
# else:
#     print("Lista zakupów jest krótka")

#zad 2
# jedzenie = float(input("Ile wydajesz na jedzenie? "))
# rozrywka = float(input("Ile wydajesz na rozrywkę? "))
# oplaty = float(input("Ile wydajesz na opłaty? "))
# inne = float(input("Ile wydajesz na inne? "))
#
# suma= jedzenie+rozrywka+oplaty+inne
# procent = {
#     "jedzenie": jedzenie*100/suma,
#     "rozrywka": rozrywka*100/suma,
#     "opłaty": oplaty*100/suma,
#     "inne": inne*100/suma
# }
# most_important = "jedzenie"
# if procent["rozrywka"] > procent[most_important]:
#     most_important = "rozrywka"
# if procent["opłaty"] > procent[most_important]:
#     most_important = "opłaty"
# if procent["inne"] > procent[most_important]:
#     most_important = "inne"
# print(f"Najwięcej wydajesz na {most_important} czyli {procent[most_important]:.2f}%")

#zad3
# matematyka = int(input("Podaj ocenę z matematyki "))
# fizyka = int(input("Podaj ocenę z fizyki "))
# chemia = int(input("Podaj ocenę z chemii "))
# biologia = int(input("Podaj ocenę z biologii "))
# jedynki = 0
# if matematyka < 2:
#     jedynki = jedynki +1
# if fizyka < 2:
#     jedynki = jedynki +1
# if chemia < 2:
#     jedynki = jedynki +1
# if biologia < 2:
#     jedynki = jedynki +1
# if jedynki == 0:
#     print("Zdajesz do kolejnej klasy")
# else:
#     if jedynki == 1:
#         srednia = ((matematyka + fizyka + chemia + biologia) / 4)
#         if srednia >= 3.5:
#             print("Zdajesz warunkowo")
#         else:
#             print("Nie zdajesz")
#     else:
#         print("Nie zdajesz")

#zad4
name = input("Podaj imię ")
if name[-1] == "a":
    print("Imię żeńskie")
else:
    print("Imię męskie")
