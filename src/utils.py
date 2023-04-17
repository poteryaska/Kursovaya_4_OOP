# from classes import *
def sort_by_salary_min(data):
    data = sorted(data, reverse=False)
    return data

def sort_by_salary_max(data):
    data = sorted(data, reverse=True)
    return data

def get_best_vacancies(vacancies, quantity):
    vacancies = sorted(vacancies, reverse=True)
    best_vacancies = vacancies[0:quantity]
    for vacancy in best_vacancies:
        print(vacancy)

# def get_vacancies_by_salary(vacancies, salary_min, salary_max):
#     for vacancy in self.select():
#         if int(vacancy.__salary_from) <= salary_min <= int(vacancy.__salary_to):
#             print(vacancy)
#         elif int(vacancy.__salary_from) <= salary_max <= int(vacancy.__salary_to):
#             print(vacancy)
