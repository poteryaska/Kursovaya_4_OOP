from utils import *
from classes import *

def main():
    while True:
        try:
            choice_platform = int(input('Выберите сайт для поиска вакансий\n'
                                'Наберите цифру:\n1, если ищем на HeadHunter\n'
                                '2, если ищем на SuperJob\n'))

            if choice_platform == 1:
                platform = HeadHunterApi()
                keyword = input('Введите одно ключевое слово для поиска вакансий\n')
                get_data = platform.get_vacancies(keyword)
                file = HHJsonSAver()
                file.add_vacancy(get_data)
                vacancies = file.select()
                print(f'Всё, что нашлось:\n')
                for vacancy in vacancies:
                    print(vacancy)
                choice_city = input('Отсортировать по городу?\n')
                if choice_city.lower() == 'да' or choice_city.lower() == 'yes':
                    city = input('Введите название города:\n')
                    print(file.get_vacancies_by_city(vacancies, city))
                else:
                    continue
                options = [{1:'Сортировать по убыванию минимальной зарплаты'},
                           {2:'Сортировать по возрастанию минимальной зарплаты'},
                           {3:'Сортировать по убыванию минимальной зарплаты'},
                           {4:'Сортировать по убыванию минимальной зарплаты'},
                           {5:'Сортировать по убыванию минимальной зарплаты'}]



            elif choice_platform == 2:
                platform = SuperJobApi()
                keyword = input('Введите одно ключевое слово для поиска вакансий\n')
                get_for_key = platform.get_vacancies(keyword)

        except ValueError:
            print('Введите только цифру 1 или 2')



    # data = a.get_vacancies('Java')
    # # print(data)
    # f = HHJsonSAver()
    # f.add_vacancy(data)
    # data = f.select()
    # print(len(data))
    # sort_by_salary_max(data)
    # # # print(type(data))
    # # # best = get_best_vacancies(data, 10)
    # # f.get_vacancies_by_salary(150000, 200000)
    # # for i in best:
    # #     print(i)
    #
    # for d in data:
    #     print(d.salary_from, end='\n')

    # f.get_vacancies_by_salary(1000, 120000)


if __name__ == "__main__":
    main()
