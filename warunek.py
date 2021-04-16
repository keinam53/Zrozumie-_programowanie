# jablka = 3
# banany = 4.5
# gruszki = 3
# print(f"Czy jabłka są droższe od bananów?\t\t\t\t {jablka>banany}")
# print(f"czy gruszki mają taką samą cenę jak banany?\t\t{gruszki==banany}")
#
# result = jablka==banany
# print(type(result))

# name = "Mariusz"
# result = name =="Mariusz"
# print(result)

# name = input("Jak masz na imię? ")
# porownanie = name == "Mariusz"
# print(f"Twoje imię to Mariusz?\t\t\t {porownanie}")

# shopping_list = ["Mąka","Jogurt"]
# my_list = ["Czekolada","Marchewka","chleb"]
# print(f"{shopping_list} > {my_list} -> {shopping_list>my_list}")

# zad1
# ceny = []
# price = float(input("Podaj cenę pierwszego produktu "))
# ceny.append(price)
# price = float(input("Podaj cenę drugiego produktu "))
# ceny.append(price)
# price = float(input("Podaj cenę trzeciego produktu "))
# ceny.append(price)
#
# print("Porównanie cen")
# print(f"Produkt 1 jest droższy do 2? {ceny[0]>ceny[1]}")
# print(f"Produkt 3 jest droższy do 1? {ceny[2]>ceny[0]}")
# print(f"Produkt 2 jest droższy do 3? {ceny[1]>ceny[2]}")

# zad2
# shopping_elements = input("Podaj listę zakupów rozdzielając elementy przecinkami ")
# shopping_list = shopping_elements.split(",")
# long = len(shopping_list) > 4
# print(f"Czy uważam, że lista zakupów jest długa?\t {long}")

#zad3
print("Kalkulator oprocentowania")
wartosc_pocz = float(input("Jaką wartość wpłaciłeś? "))
oprocentowanie = float(input("Jakie jest oprocentowanie? "))
czas = float(input("Ile lat trwa lokata? "))
wartosc_koncowa = wartosc_pocz * (1+oprocentowanie/100)**czas
zysk = wartosc_koncowa - wartosc_pocz
zysl_w_proc = (wartosc_koncowa/wartosc_pocz)*100
print(f"Zysk na lokacie wyniesie {zysk} zł")
print(f"Czy zysk na lokacie będzie większy niż 10%\t{zysl_w_proc >= 10}")


