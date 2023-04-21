from abc import ABC, abstractmethod
import json
import requests


class Job(ABC):
    """Абстрактный метод для взаимодействия через API"""

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    def __str__(self):
        return f'Данные с сайта'


class HeadHunterApi(Job):
    """Класс для работы с сайтом HeadHunter,для получения данных по вакансиям"""

    def __str__(self):
        return f'{super().__str__()} HeadHunter:'

    def get_vacancies(self, keyword: str):
        """Через API получаем данные по ключевому слову"""
        url = "https://api.hh.ru/vacancies"
        all_pages = 5
        page = 0
        all_vacancies = []
        while page < all_pages:
            params = {
                "text": keyword,
                "page": page,
                "per_page": 100
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                for vacancy in vacancies:
                    if vacancy["salary"] is not None:
                        salary_from = vacancy["salary"]["from"]
                        if salary_from is None:
                            salary_from = 0
                        salary_to = vacancy["salary"]["to"]
                        if salary_to is None:
                            salary_to = 0
                    else:
                        salary_from = 0
                        salary_to = 0
                    all_vacancies.append({
                        "name_vacancy": (vacancy["name"]).lower(),
                        "url_vacancy": (vacancy["apply_alternate_url"]).lower(),
                        "salary_from": (str(salary_from)).lower(),
                        "salary_to": (str(salary_to)).lower(),
                        "town": (vacancy["area"]["name"]).lower(),
                    })
            else:
                print("Error:", response.status_code)
            page += 1
        return all_vacancies


class SuperJobApi(Job):
    """Класс для работы с сайтом SuperJob,для получения данных по вакансиям"""

    def __str__(self):
        return f'{super().__str__()} SuperJob:'

    def get_vacancies(self, keyword: str):
        """Через API получаем данные по ключевому слову"""
        url = "https://api.superjob.ru/2.0/vacancies/"
        api_key = {
            'X-Api-App-Id': ''}
        page = 1
        page_more = True
        all_vacancies = []
        while page_more:
            params = {
                "keyword": keyword,
                "count": 100,
                "page": page
            }
            response = requests.get(url, headers=api_key, params=params)
            if response.status_code == 200:
                vacancies = response.json()["objects"]
                for vacancy in vacancies:
                    all_vacancies.append({
                        "name_vacancy": (vacancy["profession"]).lower(),
                        "url_vacancy": (vacancy["link"]).lower(),
                        "salary_from": (str(vacancy["payment_from"])).lower(),
                        "salary_to": (str(vacancy["payment_to"])).lower(),
                        "town": (vacancy["town"]["title"]).lower(),
                    })
            else:
                print("Error:", response.status_code)
            page_more = response.json()["more"]
            page += 1
        return all_vacancies


class Vacancy:
    """Базовый класс для вакансий"""
    __slots__ = ['__name_vacancy', '__url_vacancy', '__town', '__salary_from', '__salary_to']

    def __init__(self, name_vacancy: str, url_vacancy: str, town: str, salary_from: str = None, salary_to: str = None):
        self.__name_vacancy = name_vacancy
        self.__url_vacancy = url_vacancy
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__town = town

    @property
    def name_vacancy(self):
        return self.__name_vacancy

    @property
    def url_vacancy(self):
        return self.__url_vacancy

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def town(self):
        return self.__town

    def __str__(self):
        return f'Наименование вакансии: {self.__name_vacancy}\nСсылка: {self.__url_vacancy}\nГород: {self.__town}\nЗарплата от: {self.__salary_from} до {self.__salary_to} рублей\n{"--" * 200}\n'

    def __lt__(self, other):
        return int(self.__salary_from) < int(other.__salary_from)


class JSONSaver:
    def add_vacancy(self, response: list):
        '''Сохранение информации о вакансиях в файл'''
        with open("vacancies.json", "w", encoding='utf-8') as write_file:
            json.dump(response, write_file, indent=4, ensure_ascii=False)

    def select(self):
        '''Открытие файла с вакансиями для создания списка
        с экземплярами класса Vacancy для взаимодействия с пользователем'''
        try:
            with open("vacancies.json", "r", encoding='utf-8') as file:
                data = json.load(file)
            vacancies = []
            for item in data:
                vacancies.append(Vacancy(item["name_vacancy"], item["url_vacancy"], item["town"], item["salary_from"],
                                         item["salary_to"]))
            return vacancies
        except ValueError:
            print('Файл для обработки неверного формата, либо пустой')
