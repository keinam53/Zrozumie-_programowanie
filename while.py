# counter = 0
# while counter <= 30:
#     print(counter)
#     counter = counter +1

# ziemniaki = int(input("Ile chcesz ziemniaków na obiad? "))
# potatoes = []
# while len(potatoes) < ziemniaki:
#     print("Ziemniak")
#     potatoes.append("Ziemniak")
# print(potatoes)

# #Podanie liczby większej niż 100
# liczba = 0
# while liczba <= 100:
#     liczba = int(input("Podaj liczbę większą od 100 "))
#     if liczba <= 100:
#         print(f"{liczba} nie jest większa od 100")
# print("Ok")

# age = int(input("Ile masz lat? "))
# while age <= 1:
#     print("Błędny iek")
#     age = int(input("Podaj wiek ponownie "))
# if age <18:
#     print("Nie możesz jeszcze głosować")
# else:
#     print("Możesz już głosować")

# option = "t"
# while option == "t":
#     przychod = float(input("Podaj przychód firmy "))
#     ilosc_praco = int(input("Podaj liczbę pracowników "))
#     lata_na_rynku = int(input("Ile lat firma jest na rynku? "))
#     if przychod < 5000:
#         print("Główne wsparcie")
#     elif 5 <= ilosc_praco <= 10:
#         print("Wsparcie pracownicze")
#     elif lata_na_rynku < 3:
#         print("Wsparcie dla nowych firm")
#     else:
#         print("Wsparcie na pocieszenie")
#     option = input("chcesz sprawdzić dla innej firmy? (t/n) ")

# favourite_sports = ["Pływanie","Siłownia","Bieg","koszykówka"]
# index = 0
# while index < len(favourite_sports):
#     print(favourite_sports[index])
#     index = index +1

# favourite_sports = ["Pływanie","Siłownia","Bieg","koszykówka"]
# index = 0
# while index < len(favourite_sports):
#     if index %2 == 0:
#         print(favourite_sports[index])
#     index = index +1

# numbers = [4,7,9,44,756,9367]
# index = 0
# suma = 0
# while index < len(numbers):
#     suma += numbers[index]
#     index += 1
# print(f"Suma liczb wynosi {suma}")

# kod_pocztowy = input("Jaki jest twoj kod pocztowy? ")
# index = 0
#
# while index < len(kod_pocztowy):
#     print(f"[{index}] - {kod_pocztowy[index]}")
#     index += 1

#ZAD1
# liczba = int(input("Podaj liczbę parzystą "))
# proby = 1
# while proby < 10 and liczba %2 !=0:
#         liczba = int(input("Podaj liczbę parzystą "))
#         proby += 1

#ZAD2
# numer = input("Podaj swój nr.tel ")
# numer = numer.replace("-","")
# nr_sformatowany = ""
# index = 0
# while index < len(numer):
#     if index % 3 == 0 and index != 0:
#         nr_sformatowany += "-"
#     nr_sformatowany += numer[index]
#     index += 1
# print(nr_sformatowany)

#ZAD3
dania = input("Podaj ulubione dania rozdzielając przecinkiem ")
ulubione_dania = dania.split(",")
index = 0
while index < len(ulubione_dania):
    print(f"Danie nr.{index+1} - {ulubione_dania[index]}")
    index += 1

