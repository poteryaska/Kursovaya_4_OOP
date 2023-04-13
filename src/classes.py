from abc import ABC, abstractmethod
import requests
import json

class Job(ABC):
    @abstractmethod
    def connect_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass

class HeadHunterApi(Job):
    def __init__(self, url="https://api.hh.ru/vacancies"):
        self.__url = url
        self.__vacancies = []

    def connect_api(self):
        return self.__url

    def get_vacancies(self, search_text):
        params = {"text": search_text}
        response = requests.get(self.__url, params=params)
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
                self.__vacancies.append({"name_vacancy": (vacancy["name"]).lower(),
                                         "url_vacancy": (vacancy["apply_alternate_url"]).lower(),
                                         "salary_from": (str(salary_from)).lower(),
                                         "salary_to": (str(salary_to)).lower(),
                                         "town": (vacancy["area"]["name"]).lower(),
                                         })
            with open("vacancies.json", "w", encoding='utf-8') as write_file:
                json.dump(self.__vacancies, write_file, indent=4, ensure_ascii=False)
                for vacancy in self.__vacancies:
                    print(vacancy["name_vacancy"], vacancy["salary_from"])
        else:
            print("Error:", response.status_code)


class SuperJob(Job):
    def __init__(self, url="https://api.superjob.ru/2.0/vacancies/"):
        self.__url = url
        self.__vacancies = []

    def connect_api(self):
        return self.__url

    def get_vacancies(self, search_text):
        api_key = {'X-Api-App-Id': 'v3.h.4455282.7eb36007ef58eb15c52a61399870fe45fa6e854d.1fda0d61019317af27f3361fe0d54e6e149fef37'}
        params = {"keyword": search_text}
        response = requests.get(self.__url, headers=api_key, params=params)
        if response.status_code == 200:
            vacancies = response.json()["objects"]
            for vacancy in vacancies:
                self.__vacancies.append({"name_vacancy": (vacancy["profession"]).lower(),
                                         "url_vacancy": (vacancy["link"]).lower(),
                                         "salary_from": (str(vacancy["payment_from"])).lower(),
                                         "salary_to": (str(vacancy["payment_to"])).lower(),
                                         "town": (vacancy["town"]["title"]).lower(),
                                         })
            with open("vacancies_SJ.json", "w", encoding='utf-8') as write_file:
                json.dump(self.__vacancies, write_file, indent=4, ensure_ascii=False)
                for vacancy in self.__vacancies:
                    print(vacancy["name_vacancy"], vacancy["salary_from"])
        else:
            print("Error:", response.status_code)

# v = HeadHunterApi()
# v.get_vacancies('репетитор')
# print('--------------------------------')
# a = SuperJob()
# a.get_vacancies('репетитор')

class Vacancy:
    def __init__(self, name_vacancy, url_vacancy, town, salary_from:str=None, salary_to=None):
        self.__name_vacancy = name_vacancy
        self.__url_vacancy = url_vacancy
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__town = town
    def __str__(self):
        return f'{self.__name_vacancy}, {self.__url_vacancy}, {self.__town}, {self.__salary_from}, {self.__salary_to}'
    def __gt__(self, other):
        if self.__salary_from and other.__salary_from is not None:
            if int(self.__salary_from) > int(other.__salary_from):
                return f'В этой вакансии: {self.__name_vacancy} БОЛЬШЕ мin зарплата, чем тут: {other.__name_vacancy}'
            else:
                return f'В этой вакансии: {self.__name_vacancy} МЕНЬШЕ мin зарплата, чем тут: {other.__name_vacancy}'
        else:
            raise ValueError('Отсутствуют данные о зарплате')
    def __lt__(self, other):
        if int(self.__salary_from) < int(other.__salary_from):
            return f'В этой вакансии: {self.__name_vacancy} МЕНЬШЕ мin зарплата, чем тут: {other.__name_vacancy}'

vacancy1 = Vacancy('учитель', 'https://hh.ru/applicant/vacancy_response?vacancyid=78853115', 'москва')
vacancy2 = Vacancy('учитель', 'https://hh.ru/applicant/vacancy_response?vacancyid=78853115', 'москва')
print(vacancy1)
print(vacancy1 > vacancy2)

class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(Saver):
    def add_vacancy(self, vacancy):
        pass


