#słownik polsko-angielski
# polish_to_english={
#     "amnezja": "amnesia",
#     "aktywista": "activist",
#     "burza": "storm"
# }
# print("Słownik polsko-angielski: ",polish_to_english)
# print(f"Burza po angielsku to {polish_to_english['burza']}")
# #Różne typy
# expenditures = {
#     "prąd": 250,
#     "woda": 30.45,
#     "zakupy": [
#         120.15,
#         170.53,
#         20.15
#     ]
# }
# print(expenditures)
# print(expenditures["zakupy"])
#
# #słownik zawierający słownik
teacher = {
    "first_name": "Jan",
    "last_name": "Kowalski",
    "age": 45,
    "contract": {
        "sign_date": "23.11.2018",
        "salary": 3500
    }
}
print(teacher)
# teacher["first_name"] = "Marcin"
# # print(teacher)
# #Dodawanie
# teacher["city"] = "Gdańsk"
# # print(teacher)
# #usuwanie
# del teacher["first_name"]
# # print(teacher)
# #metody keys oraz values
print(teacher.values())
print(teacher.keys())
# #funkcja list
keys = list(teacher.keys())
values = list(teacher.values())
print(keys,values, sep="\n")
# #liczba elementów
# print(len(teacher))

# students = [
#     {
#         "first_name": "Patryk",
#         "last_name": "Nowak"
#     },
#     {
#         "first_name": "Alicja",
#         "last_name": "Kowalska"
#     }
# ]
# print(students[0]["first_name"])

#ZAD 1
# oceny = {
#     "matematyka": 4,
#     "fizyka": 3,
#     "biologia": 5
# }
# print(oceny)

#ZAD 2
# my_family = {
#     "first_name": "Mariusz",
#     "last_name": "Baran",
#     "birth_date": "27.08.1994",
#     "parents": [
#     {
#     "first_name": "Wojciech",
#     "last_name": "Baran",
#     "birth_date": "10.04.1965"
#     },{
#     "first_name": "Elżbieta",
#     "last_name": "Baran",
#     "birth_date": "07.07.1967"
#         }
#     ]
# }
# print(my_family["parents"])

# ZAD 3
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
# kategoria = input("Wybierz kategorię (jedzenie, rozrywka, opłaty, inne) ")
# print(f"Na {kategoria} wydajesz {procent[kategoria]:.0f}% wszystkich wydatków")