# def best_grades(grades, best_grade_number):
#     grades.sort(reverse=True)
#     if best_grade_number < len(grades):
#         return grades[:best_grade_number]
#     else:
#         print("Zwrócone zostaną wszystkie")
#     return grades
# math_grades = [3, 2, 5, 3, 4, 2]
# print(best_grades(math_grades, best_grade_number=2))

# def write_final_grades(subject_grades, final_grades=None):
#     if final_grades is None:
#         final_grades = []
#     grades_avg = sum(subject_grades) / len(subject_grades)
#     final_grades.append(int(grades_avg))
#     return final_grades
# mariusz_math = [5, 3, 4, 2, 5, 4]
# mariusz_fiz = [3, 4, 2, 5, 1, 4]
# mariusz_final = write_final_grades(subject_grades=mariusz_math)
# mariusz_final = write_final_grades(subject_grades=mariusz_fiz, final_grades=mariusz_final)
# print(f"Oceny Mariusza: {mariusz_final}")
#
# marcin_math = [5, 3, 4, 5, 5, 5]
# marcin_fiz = [1, 4, 2, 3, 1, 4]
# marcin_final = write_final_grades(subject_grades=marcin_math)
# marcin_final = write_final_grades(subject_grades=marcin_fiz, final_grades=marcin_final)
# print(f"Oceny Marcina: {marcin_final}")

#ZAD1
# def zakresy(liczba):
#     plus = liczba + 0.1 * liczba
#     minus = liczba - 0.1 * liczba
#     zakres = [minus, plus]
#     return zakres
# print(zakresy(200))

#ZAD2
def dodawanie_imion(imiona, lista=None):
    if lista is None:
        lista = []
    imie = imiona.split(",")
    for i in imie:
        lista.append(i)
    return lista
imiona_kandydatow = "Marcin,Jan,Kamil,Emil"
kurs_poniedzialkowy = dodawanie_imion(imiona_kandydatow)
print(kurs_poniedzialkowy)
imiona_kandydatow = "Ola,Jacek"
kurs_poniedzialkowy = dodawanie_imion(imiona_kandydatow, lista=kurs_poniedzialkowy)
print(kurs_poniedzialkowy)

