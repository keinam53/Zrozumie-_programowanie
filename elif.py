# przychod = float(input("Podaj przychód firmy "))
# ilosc_praco = int(input ("Podaj liczbę pracowników "))
# lata_na_rynku = int(input("Ile lat firma jest na rynku? "))
# # if przychod < 5000:
#     print("Główne wsparcie")
# else:
#     if 5 <= ilosc_praco <= 10:
#         print("Wsparcie pracownicze")
#     else:
#         if lata_na_rynku < 3:
#             print("Wsparcie dla nowych firm")
#         else:
#             print("Wsparcie na pocieszenie")

# TO SAMO Z ELIF

# if przychod < 5000:
#     print("Główne wsparcie")
# elif 5 <= ilosc_praco <= 10:
#     print("Wsparcie pracownicze")
# elif lata_na_rynku < 3:
#     print("Wsparcie dla nowych firm")
# else:
#     print("Wsparcie na pocieszenie")

#ZAD1
# print("Kalkulator lokaty - 1", "kalkualtor kredytowy - 2", sep="\n")
# option = input("Wybierz opcję: ")
# if option == "1":
#     wartosc_pocz = float(input("Jaką wartość wpłaciłeś? "))
#     oprocentowanie = float(input("Jakie jest oprocentowanie? "))
#     czas = float(input("Ile lat trwa lokata? "))
#     wartosc_koncowa = wartosc_pocz * (1+oprocentowanie/100)**czas
#     zysk = wartosc_koncowa - wartosc_pocz
#     zysl_w_proc = (wartosc_koncowa/wartosc_pocz)*100
#     print(f"Zysk na lokacie wyniesie {zysk} zł")
#     print(f"Czy zysk na lokacie będzie większy niż 10%\t{zysl_w_proc >= 10}")
# elif option == "2":
#     kwota_kredytu = float(input("Podaj kwotę kredytu "))
#     oprocentowanie = float(input("Podaj oprocentowanie "))
#     wklad_wl = float(input("Podaj wkład własny "))
#     czas = float(input("Podaj czas trwania kredytu w latach "))
#     przychod_mies = float(input("Podaj twój miesięczny przychód "))
#     wydatki_mies = float(input("Podaj twoje miesięczne wydatki "))
#     rata = (kwota_kredytu * oprocentowanie / 100) / 12 + kwota_kredytu / (czas * 12)
#     srodki = przychod_mies - wydatki_mies
#     wartosc = wklad_wl + kwota_kredytu
#
#     czesc_wkladu = wklad_wl/wartosc
#     srodki_bez_wydatkow = srodki - rata
#
#     if czesc_wkladu >= 0.2 and srodki_bez_wydatkow >= 1000:
#         print("Możesz wziąć kredyt (wariant 1)")
#     else:
#         if 0.1 <= czesc_wkladu <= 0.2 and srodki_bez_wydatkow >= 2000:
#             print("Możesz wziąć kredyt (wariant 2)")
#         else:
#             print("Nie możesz")
# else:
#     print ("Zły wybór")

#ZAD2
wiek = int(input("Podaj swój wiek "))
plec = input("Podaj swoją płeć (k/m) ")
wynik = int(input("Twój wynik "))
if plec == "m":
    if wiek == 8:
        if wynik >= 2190:
            print("Bardzo dobrze")
        elif 1810 < wynik:
            print("Dobrze")
        elif 1420 < wynik:
            print("Srednio")
        elif 1050 < wynik:
            print("Żle")
        else:
            print("Bardzo źle")
    else:
        if wiek == 9:
            if wynik >= 2350:
                print("Bardzo dobrze")
            elif 1950 < wynik:
                print("Dobrze")
            elif 1540 < wynik:
                print("Srednio")
            elif 1130 < wynik:
                print("Żle")
            else:
                print("Bardzo źle")
else:
    if plec == "k":
        if wiek == 8:
            if wynik >= 2120:
                print("Bardzo dobrze")
            elif 1770 < wynik:
                print("Dobrze")
            elif 1400 < wynik:
                print("Srednio")
            elif 1050 < wynik:
                print("Żle")
            else:
                print("Bardzo źle")
        else:
            if wiek == 9:
                if wynik >= 2190:
                    print("Bardzo dobrze")
                elif 1810 < wynik:
                    print("Dobrze")
                elif 1420 < wynik:
                    print("Srednio")
                elif 1050 < wynik:
                    print("Żle")
                else:
                    print("Bardzo źle")

    else:
        print("Błędna płeć")

