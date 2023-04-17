from utils import *
from classes import *

def main():
    a = SuperJob()
    a.connect_api('Python')
    data = a.get_vacancies('Python')
    # print(data)
    f = JSONSaver()
    f.add_vacancy(data)
    data = f.select()
    # data = sort_by_salary_max(data)
    # # print(type(data))
    # # best = get_best_vacancies(data, 10)
    # f.get_vacancies_by_salary(150000, 200000)
    # for i in best:
    #     print(i)
    #
    # for d in data:
    #     print(d.salary_from, end='\n')

    # f.get_vacancies_by_salary(1000, 120000)


if __name__ == "__main__":
    main()
