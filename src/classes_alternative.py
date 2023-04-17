from abc import ABC, abstractmethod
import requests
import json

class Job(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunterApi(Job):

    def get_vacancies(self, keyword):
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


class SuperJob(Job):
    def connect_api(self, keyword, page=1):
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

    # def __gt__(self, other):
    #     if self.__salary_from and other.__salary_from is not None:
    #         if int(self.__salary_from) > int(other.__salary_from):
    #             return f'В этой вакансии: {self.__name_vacancy} БОЛЬШЕ мin зарплата, чем тут: {other.__name_vacancy}'
    #         else:
    #             return f'В этой вакансии: {self.__name_vacancy} МЕНЬШЕ мin зарплата, чем тут: {other.__name_vacancy}'
    #     else:
    #         raise ValueError('Отсутствуют данные о зарплате')

    def __lt__(self, other):
        if int(self.__salary_from) < int(other.__salary_from):
            return self.__name_vacancy


# vacancy1 = Vacancy('учитель', 'https://hh.ru/applicant/vacancy_response?vacancyid=78853115', 'москва')
# vacancy2 = Vacancy('учитель', 'https://hh.ru/applicant/vacancy_response?vacancyid=78853115', 'москва')
# print(vacancy1)
# print(vacancy1 > vacancy2)

class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, data):
        pass
#
#     @abstractmethod
#     def get_vacancies_by_salary(self):
#         pass
#
#     @abstractmethod
#     def delete_vacancy(self):
#         pass


class JSONSaver(Saver):
    def add_vacancy(self, response):
        with open("Python.json", "w", encoding='utf-8') as write_file:
            json.dump(response, write_file, indent=4, ensure_ascii=False)


    def select(self):
        with open("Python.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        vacancies = []
        for item in data:
            vacancies.append(Vacancy(item["name_vacancy"], item["url_vacancy"], item["town"], item["salary_from"], item["salary_to"]))
        return vacancies

    def get_vacancies_by_salary(self, salary_min, salary_max):
        for vacancy in self.select():

            if (int(vacancy.salary_from) >= salary_min) and (salary_min <= int(vacancy.salary_to) <= salary_max):
                # if int(vacancy.salary_to) == 0:

                print(vacancy)

a = SuperJob()


data = a.get_vacancies('Python')
# print(data)
f = JSONSaver()
f.add_vacancy(data)
data = f.select()
f.get_vacancies_by_salary(15000, 200000)


# # best = get_best_vacancies(data, 10)
# f.get_vacancies_by_salary(150000, 200000)
# for d in data:
#     print(d, end='\n')

def sort_by_salary_min(data):
    data = sorted(data, reverse=False)
    return data

def sort_by_salary_max(data):
    data = sorted(data, reverse=True)
    return data

# data1 = sort_by_salary_max(data)
#
# print(len(data1))