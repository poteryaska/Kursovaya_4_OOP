from utils import *
from classes import *

def main():
    '''Взаимодействие с пользователем'''
    # while True:
    try:
        choice_platform = int(input('Выберите сайт для поиска вакансий\n'
                            'Наберите цифру:\n1, если ищем на HeadHunter\n'
                            '2, если ищем на SuperJob\n').replace(' ', ''))

        if choice_platform == 1:
            platform = HeadHunterApi()
            keyword = input('Введите одно ключевое слово для поиска вакансий\n')
            get_data = platform.get_vacancies(keyword)
            file = JSONSaver()
            file.add_vacancy(get_data)
            vacancies = file.select()
            print(platform)
            print(f'Всё, что нашлось:\n')
            for vacancy in vacancies:
                print(vacancy)
            choice_city = int(input('Отсортировать по городу?\n'
                                'Наберите цифру:\n1 - да\n2 - нет\n').replace(' ', ''))
            if choice_city == 1:
                city = input('Введите название города:\n')
                vacancies_by_city = get_vacancies_by_city(vacancies, city)
                for vacancy in vacancies_by_city:
                    print(vacancy)
                other_sorties = int(input('Выберите сортировку:\nВведите сооответствующую цифру:\n'
                                          '1 - Сортировать по убыванию минимальной зарплаты\n'
                                          '2 - Сортировать по возрастанию минимальной зарплаты\n').replace(' ', ''))
                if other_sorties == 1:
                    max_sort = sort_by_salary_max(vacancies_by_city)
                    for vacancy in max_sort:
                        print(vacancy)
                elif other_sorties == 2:
                    min_sort = sort_by_salary_min(vacancies_by_city)
                    for vacancy in min_sort:
                        print(vacancy)

            elif choice_city == 2:
                print('Имеются и другие варианты сортировки:')
                other_sorties = int(input('Выберите сортировку:\nВведите цифру, сооответствующую запросу:\n'
                                      '1 - Сортировать по убыванию минимальной зарплаты\n'
                                      '2 - Сортировать по возрастанию минимальной зарплаты\n').replace(' ', ''))
                if other_sorties == 1:
                    max_sort = sort_by_salary_max(vacancies)
                    for vacancy in max_sort:
                        print(vacancy)
                elif other_sorties == 2:
                    min_sort = sort_by_salary_max(vacancies)
                    for vacancy in min_sort:
                        print(vacancy)
                # else:



            # if choice_city.lower() == 'да' or choice_city.lower() == 'yes':
            #     city = input('Введите название города:\n')
            #     vacancies_by_city = get_vacancies_by_city(vacancies, city)
            #     for vacancy in vacancies_by_city:
            #         print(vacancy)
            # elif choice_city.lower() == 'нет' or choice_city.lower() == 'no':


                # if other_sorties == 1:
                #     sort_by_salary_max(data)
            else:
                print('Выберите другую сортировку:\nВведите цифру, сооответствующую запросу:\n'
                      '1 - Сортировать по убыванию минимальной зарплаты\n'
                      '2 - Сортировать по возрастанию минимальной зарплаты\n'
                      '3 - Сортировать по минимальной и максимальной суммой зарплаты\n')



        # elif choice_platform == 2:
        #     platform = SuperJobApi()
        #     keyword = input('Введите одно ключевое слово для поиска вакансий\n')
        #     get_for_key = platform.get_vacancies(keyword)

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
