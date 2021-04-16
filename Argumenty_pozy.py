# def add_two_number(first_num, second_num):
#     print(f"Pierwsza liczba: {first_num}")
#     print(f"Druga liczba: {second_num}")
#     return first_num + second_num
# print(add_two_number(2, 4))
# print(add_two_number(4, 2))

#ZAD1
# def predkosc_srednia(dystans, czas):
#     predkosc = dystans / czas
#     return predkosc
# def predkosc_srednia_main(nazwa_poj):
#     dystans = float(input(f"Jaki dystans pokonałeś poruszając się {nazwa_poj}? "))
#     czas = float(input("W jakim czasie? "))
#     predkosc = predkosc_srednia(dystans=dystans, czas=czas)
#     print(f"Twoja prędkość wynosiła {predkosc:.2f} km/h poruszając się {nazwa_poj}")
# predkosc_srednia_main(nazwa_poj="biegiem")
# predkosc_srednia_main(nazwa_poj="rowerem")
# predkosc_srednia_main(nazwa_poj="samochodem")

# def print_name():
#     print(name)
# name = "Mariusz"
# print_name()

PI_NUMBER = 3.141
def pole_kola(promien):
    pole = PI_NUMBER * promien * promien
    return pole
print(pole_kola(promien=2))
