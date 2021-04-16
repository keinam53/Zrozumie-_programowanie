# name = input("Podaj swoje imię ")
# print("Miło Cię poznać ", name)
# name_len = len(name)
# if name_len < 5:
#     print(name, "to imię krótkie")
# else:
#     if name_len >= 5 and name_len <=8:
#         print(name, "to imię średniej długości")
#     else:
#         print(name, "to imię długie")

# born_in_usa = input("Czy jesteś urodzony w USA? (t/n) ")
# age = int(input("Ile masz lat? "))
# residence = int(input("Ile lat mieszkasz w USA? "))
# if born_in_usa == "t":
#     born_in_usa = True
# else:
#     born_in_usa = False
# if born_in_usa and age >= 35 and residence >= 14:
#     print("Możesz kandydować")
# else:
#     print("Nie możesz kandydować")

# przychod = int(input("Podaj miesięczny przychód firmy "))
# pracownicy = int(input("Ilu pracowników zatrudniasz? "))
# inne_dot = input("Czy firma otrzymała już inne dotacje? (t/n) ")
# if inne_dot == "t":
#     inne_dot = True
# else:
#     inne_dot = False
# if not inne_dot and (przychod <= 15500 or pracownicy >= 3):
#     print("Otrzymasz dotację")
# else:
#     print("Nie otrzymasz dotacji")

#zad1
kwota_kredytu = float(input("Podaj kwotę kredytu "))
oprocentowanie = float(input("Podaj oprocentowanie "))
wklad_wl = float(input("Podaj wkład własny "))
czas = float(input("Podaj czas trwania kredytu w latach "))
przychod_mies = float(input("Podaj twój miesięczny przychód "))
wydatki_mies = float(input("Podaj twoje miesięczne wydatki "))
rata = (kwota_kredytu * oprocentowanie / 100) / 12 + kwota_kredytu / (czas * 12)
srodki = przychod_mies - wydatki_mies
wartosc = wklad_wl + kwota_kredytu

czesc_wkladu = wklad_wl/wartosc
srodki_bez_wydatkow = srodki - rata

if czesc_wkladu >= 0.2 and srodki_bez_wydatkow >= 1000:
    print("Możesz wziąć kredyt (wariant 1)")
else:
    if 0.1 <= czesc_wkladu <= 0.2 and srodki_bez_wydatkow >= 2000:
        print("Możesz wziąć kredyt (wariant 2)")
    else:
        print("Nie możesz")



