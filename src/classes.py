from abc import ABC, abstractmethod
import requests
import json

class Job(ABC):
    @abstractmethod
    def connect_api(self, keyword, page):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunterApi(Job):
    def connect_api(self, keyword, page=1):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,
            "page": page,
            "per_page": 100
        }
        return requests.get(url, params=params)

    def get_vacancies(self, keyword):
        response = []
        if self.connect_api(keyword).status_code == 200:
            vacancies = self.connect_api(keyword).json()["items"]
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
                response.append({
                    "name_vacancy": (vacancy["name"]).lower(),
                     "url_vacancy": (vacancy["apply_alternate_url"]).lower(),
                     "salary_from": (str(salary_from)).lower(),
                     "salary_to": (str(salary_to)).lower(),
                     "town": (vacancy["area"]["name"]).lower(),
                })
        else:
            print("Error:", self.connect_api(keyword).status_code)
        return response


class SuperJob(Job):
    def connect_api(self, keyword, page=6):
        url = "https://api.superjob.ru/2.0/vacancies/"
        api_key = {'X-Api-App-Id': 'v3.h.4455282.7eb36007ef58eb15c52a61399870fe45fa6e854d.1fda0d61019317af27f3361fe0d54e6e149fef37'}
        params = {
            "keyword": keyword,
            "page": page,
            "count": 100
        }
        return requests.get(url, headers=api_key, params=params)

    def get_vacancies(self, keyword):
        response = []
        if self.connect_api(keyword).status_code == 200:
            vacancies = self.connect_api(keyword).json()["objects"]
            for vacancy in vacancies:
                response.append({
                    "name_vacancy": (vacancy["profession"]).lower(),
                     "url_vacancy": (vacancy["link"]).lower(),
                     "salary_from": (str(vacancy["payment_from"])).lower(),
                     "salary_to": (str(vacancy["payment_to"])).lower(),
                     "town": (vacancy["town"]["title"]).lower(),
                })
        else:
            print("Error:", self.connect_api(keyword).status_code)
        return response

# v = HeadHunterApi()
# v.get_vacancies('репетитор')
print('--------------------------------')
# a = SuperJob()
# a.connect_api('Python')
# print(a.get_vacancies('Python'))

class Vacancy:
    __slots__ = ['__name_vacancy', '__url_vacancy', '__town', '__salary_from', '__salary_to']

    def __init__(self, name_vacancy, url_vacancy, town, salary_from=None, salary_to=None):
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
        return f'{self.__name_vacancy}: {self.__url_vacancy}, {self.__town} \nзп от:{self.__salary_from} до {self.__salary_to} рублей'

    def __lt__(self, other):
        if int(self.__salary_from) < int(other.__salary_from):
            return self.__salary_from



class JSONSaver:
    def add_vacancy(self, response):
        with open("vacancies.json", "w", encoding='utf-8') as write_file:
            json.dump(response, write_file, indent=4, ensure_ascii=False)

    def select(self):
        with open("vacancies.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        vacancies = []
        for item in data:
            vacancies.append(Vacancy(item["name_vacancy"], item["url_vacancy"], item["town"], item["salary_from"], item["salary_to"]))
        return vacancies

    def get_vacancies_by_salary(self, salary_min, salary_max):
        for vacancy in self.select():
            if int(vacancy.__salary_from) <= salary_min <= int(vacancy.__salary_to):
                print(vacancy)
            elif int(vacancy.__salary_from) <= salary_max <= int(vacancy.__salary_to):
                print(vacancy)



    def delete_vacancy(self):
        pass