from utils import *
from classes import *

def main():
    a = HeadHunterApi()
    a.connect_api('Python')
    data = a.get_vacancies('Python')
    # print(data)
    f = JSONSaver()
    f.add_vacancy(data)
    # data = f.select()
    # data = sort_by_salary_max(data)
    # print(type(data))

    # for d in data:
    #     print(type(d), end='\n')

    f.get_vacancies_by_salary(1000, 120000)


if __name__ == "__main__":
    main()
