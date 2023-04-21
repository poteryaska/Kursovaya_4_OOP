def get_vacancies_by_city(vacancies: list, city: str):
    '''Получаем вакансии по наименованию введенного города'''
    result = [vacancy for vacancy in vacancies if vacancy.town == city.lower()]
    return result


def sort_by_salary_min(vacancies: list):
    '''Сортировка вакансий по возрастанию минимальной зарплаты'''
    vacancies = sorted(vacancies, reverse=False)
    return vacancies


def sort_by_salary_max(vacancies: list):
    '''Сортировка вакансий по убыванию минимальной зарплаты'''
    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def get_best_vacancies(vacancies: list, quantity='10'):
    '''Получаем лучшие вакансии по минимальной зарплате'''
    vacancies = sorted(vacancies, reverse=True)
    best_vacancies = vacancies[0:int(quantity)]
    for vacancy in best_vacancies:
        print(vacancy)
