# #Definicja funkcji
# def peel_the_potatoes():
#     expected_potatoes = int(input("Ile ziemniaków potrzeba? "))
#     potatoes = []
#     while len(potatoes) < expected_potatoes:
#         print(f"{len(potatoes) + 1} ziemniak do garnka")
#         potatoes.append("Ziemniak")
# #wywołanie funkcji
# # peel_the_potatoes()
# def make_soup():
#     print("Jest zupa!")
# peel_the_potatoes()
# make_soup()

# def put_a_brick():
#     print("-", sep="", end="")
# def build_a_wall(wall_lenght):
#     # wall_lenght = int(input("Długość ściany: "))
#     for brick in range(wall_lenght):
#         put_a_brick()
#     print()
# build_a_wall(20)
# build_a_wall(5)
# build_a_wall(45)

#Funkcje z parametrami
# def function_with_params(cos,cos_innego):
#     print(cos)
#     print(cos_innego)
# #function_with_params(1,4)
# list = ["Lista", "z", "elementami"]
# dict = {"Klucz", "Wartość"}
# function_with_params(list, dict)

# def investment_value(years, procent, initial_value):
#     result = initial_value * (1 + procent / 100) ** years
#     print(f"Po {years:.0f} latach będziemy mieć {result:.2f} zł")
# print("Kalkulator oprocentowania")
# initial_value = float(input("Jaką wartość wpłaciłeś? "))
# procent = float(input("Jakie jest oprocentowanie? "))
# years = float(input("Ile lat trwa lokata? "))
# investment_value(years, procent, initial_value)

# def investment_value(years, procent, initial_value):
#     result = initial_value * (1 + procent / 100) ** years
#     return result
# def run_calculator():
#     print("Kalkulator oprocentowania")
#     initial_value = float(input("Jaką wartość wpłaciłeś? "))
#     procent = float(input("Jakie jest oprocentowanie? "))
#     years = float(input("Ile lat trwa lokata? "))
#     final_value = investment_value(years, procent, initial_value)
#     print(f"Po {years} latach na kącie będzie {final_value:.2f} zł ")
#     longer_term = years * 2
#     alternative_value = investment_value(longer_term, procent, initial_value)
#     print(f"Rozważ pozostawienie lokaty na {longer_term} lat. Będzie wtedy {alternative_value:.2f} zł")
# option = None
# while option != "X":
#     run_calculator()
#     option = input("Jeśli chcesz zakończyć wpisz X ")

# def find_best_grade(grades_by_subject):
#     best_subject = None
#     best_grade = 0
#     for subject, grade in grades_by_subject.items():
#         best_grade_from_sub = max(grade)
#         if best_grade_from_sub > best_grade:
#             best_grade = best_grade_from_sub
#             best_subject = subject
#     return best_grade, best_subject
# grades_data = {
#     "Historia": [5, 2, 4, 3, 1],
#     "Matematyka": [5, 6, 2, 3, 4],
#     "Fizyka": [2, 3, 4, 2, 3]
# }
# best_grade, best_subject = find_best_grade(grades_data)
# print(f"Najlepsza ocena to {best_grade} z {best_subject}")
# result = find_best_grade(grades_data)
# print(result)

# ZAD1
# def pole_prostokata(a, b):
#     pole = a*b
#     return pole
# a = float(input("Podaj pierwszy bok: "))
# b = float(input("Podaj drugi bok: "))
# pole = pole_prostokata(a, b)
# print(f"Pole prostokąta wynosi {pole}")

#ZAD2
# def predkosc_srednia(dystans, czas):
#     predkosc = dystans / czas
#     return predkosc
# def predkosc_srednia_main(nazwa_poj):
#     dystans = float(input(f"Jaki dystans pokonałeś poruszając się {nazwa_poj}? "))
#     czas = float(input("W jakim czasie? "))
#     predkosc = predkosc_srednia(dystans, czas)
#     print(f"Twoja prędkość wynosiła {predkosc:.2f} km/h poruszając się {nazwa_poj}")
# predkosc_srednia_main("biegiem")
# predkosc_srednia_main("rowerem")
# predkosc_srednia_main("samochodem")

#ZAD 3
print("Kalkulator budżetu miesięcznego")

def load_expenditures(category_name):
    expenditures_values = []
    while True:

        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
        if expenditure == "X":
            return expenditures_values

        expenditure_value = float(expenditure)
        expenditures_values.append(expenditure_value)


def load_expenditures_by_categories():
    expenditures = {}
    while True:
        category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
        if category_name == "X":
            return expenditures

        expenditures[category_name] = load_expenditures(category_name)


def calculate_total_expenditures(expenditures):
    result = 0
    for category_expenditures in expenditures.values():
        result += sum(category_expenditures)
    return result


def calculate_expenditures_percentages(expenditures, total_expenditures):
    percentages_by_category_name = {}
    for category_name, category_expenditures in expenditures.items():
        total_category_expenditures = sum(category_expenditures)
        percentages_by_category_name[category_name] = total_category_expenditures * 100 / total_expenditures
    return percentages_by_category_name


def find_most_important_category(percentages_by_category_name):
    highest_percentage_category = None
    highest_percentage = 0
    for category, percentage in percentages_by_category_name.items():
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_percentage_category = category
    return highest_percentage_category, highest_percentage


def print_most_important_category_info(category_name, percentage):
    print(f"Najwięcej wydajesz na {category_name} - {percentage:.0f}% wszystkich wydatków")


def print_category_info(category, percentage):
    print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")


expenditures_by_categories = load_expenditures_by_categories()
total_expenditures = calculate_total_expenditures(expenditures_by_categories)
expenditures_percentage = calculate_expenditures_percentages(expenditures_by_categories, total_expenditures)
most_important_category, most_important_category_percentage = find_most_important_category(expenditures_percentage)

if most_important_category is not None:
    print_most_important_category_info(most_important_category, most_important_category_percentage)

for category, percentage in expenditures_percentage.items():
    print_category_info(category, percentage)
