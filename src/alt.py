from utils import *
from classes import *

def main():
    '''Взаимодействие с пользователем'''
    try:
        while True:

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
                print(f'Всё, что нашлось:\n')
                for vacancy in vacancies:
                    print(vacancy)
                while True:
                    choice_city = int(input('Отсортировать по городу?\n'
                                            'Наберите цифру:\n1 - да\n2 - нет\n').replace(' ', ''))
                    if choice_city == 1:
                        city = input('Введите название города:\n')
                        vacancies_by_city = get_vacancies_by_city(vacancies, city)
                        for vacancy in vacancies_by_city:
                            print(vacancy)

                        while True:
                            other_sorties = int(input('Выберите сортировку:\nВведите сооответствующую цифру:\n'
                                                      '1 - Сортировать по убыванию минимальной зарплаты\n'
                                                      '2 - Сортировать по возрастанию минимальной зарплаты\n').replace(' ', ''))

                            if other_sorties == 1:
                                max_sort = sort_by_salary_max(vacancies_by_city)
                                for vacancy in max_sort:
                                    print(vacancy)
                                break
                            elif other_sorties == 2:
                                min_sort = sort_by_salary_min(vacancies_by_city)
                                for vacancy in min_sort:
                                    print(vacancy)
                                break
                            else:
                                print('Введите только цифру 1 или 2')

                        while True:
                            best_vacancies = int(input('Вывести лучшие 10 вакансий по зарплате?\nВведите цифру:\n'
                                                       '1 - Да\n'
                                                       '2 - Нет, этого достаточно\n').replace(' ', ''))
                            if best_vacancies == 1:
                                get_best_vacancies(vacancies_by_city)
                                break
                            elif best_vacancies == 2:
                                print('')
                                break
                            else:
                                print('Введите только цифру 1 или 2')


                    elif choice_city == 2:
                        print('Имеются и другие варианты сортировки:')
                        while True:
                            other_sorties = int(input('Выберите сортировку:\nВведите цифру, сооответствующую запросу:\n'
                                                  '1 - Сортировать по убыванию минимальной зарплаты\n'
                                                  '2 - Сортировать по возрастанию минимальной зарплаты\n').replace(' ', ''))
                            if other_sorties == 1:
                                max_sort = sort_by_salary_max(vacancies)
                                for vacancy in max_sort:
                                    print(vacancy)
                                break
                            elif other_sorties == 2:
                                min_sort = sort_by_salary_max(vacancies)
                                for vacancy in min_sort:
                                    print(vacancy)
                                break
                            else:
                                print('Введите только цифру 1 или 2')
                        while True:
                            best_vacancies = int(input('Вывести лучшие 10 вакансий по зарплате?\nВведите цифру:\n'
                                                      '1 - Да\n'
                                                      '2 - Нет, этого достаточно\n').replace(' ', ''))
                            if best_vacancies == 1:
                                get_best_vacancies(vacancies)
                                break
                            elif best_vacancies == 2:
                                print('')
                                break
                            else:
                                print('Введите только цифру 1 или 2')
                        break
                break
            # else:
            #         print('Введите только цифру 1 или 2')



                # except ValueError or TypeError:
                #     print('Введите только цифру 1 или 1111')
                # best_vacancies = int(input('Вывести лучшие 10 вакансий по зарплате?\nВведите цифру:'
                #                           '1 - Да\n'
                #                           '2 - Нет, этого достаточно\n').replace(' ', ''))
                # if best_vacancies == 1:
                #     get_best_vacancies(vacancies)
                # elif best_vacancies == 2:
                #     print('')


            elif choice_platform == 2:
                platform = SuperJobApi()
                keyword = input('Введите одно ключевое слово для поиска вакансий\n')
                get_for_key = platform.get_vacancies(keyword)
        #
    except ValueError:
        print('Введите только цифру ')



if __name__ == "__main__":
    main()