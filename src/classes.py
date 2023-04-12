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

    def connect_api(self):
        return self.__url

    def get_vacancies(self, search_text):
        params = {"text": search_text}
        response = requests.get(self.__url, params=params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            with open("vacancies.json", "w", encoding='utf-8') as write_file:
                json.dump(vacancies, write_file, indent=4, ensure_ascii=False)
            for vacancy in vacancies:
                print(vacancy["name"], vacancy["url"])
        else:
            print("Error:", response.status_code)

class SuperJob(Job):
    def __init__(self, url="https://api.superjob.ru/2.0/vacancies/"):
        self.__url = url

    def connect_api(self):
        return self.__url

    def get_vacancies(self, search_text):
        api_key = {'X-Api-App-Id': 'v3.h.4455282.7eb36007ef58eb15c52a61399870fe45fa6e854d.1fda0d61019317af27f3361fe0d54e6e149fef37'}
        params = {"keyword": search_text}
        response = requests.get(self.__url, headers=api_key, params=params)
        if response.status_code == 200:
            vacancies = response.json()["objects"]
            for vacancy in vacancies:
                vacancy["name_vacancy"] = vacancy.pop("profession")
                vacancy["url_vacancy"] = vacancy.pop("link")
                vacancy["salary_from"] = vacancy.pop("payment_from")
                vacancy["salary_to"] = vacancy.pop("payment_to")
                vacancy["salary_to"] = vacancy.pop("payment_to")
            with open("vacancies_SJ.json", "w", encoding='utf-8') as write_file:
                json.dump(vacancies, write_file, indent=4, ensure_ascii=False)
                for vacancy in vacancies:
                    print(vacancy["name_vacancy"], vacancy["salary_from"])
            # with open("vacancies_SJ.json", "w", encoding='utf-8') as write_file:
            #     json.dump(vacancies, write_file, indent=4, ensure_ascii=False)
            # for vacancy in vacancies:
            #     vacancy["name_vacancy"] = vacancy.pop("profession")
            #     vacancy["url_vacancy"] = vacancy.pop("link")
            #     print(vacancy["name_vacancy"], vacancy["url_vacancy"])
        else:
            print("Error:", response.status_code)

v = HeadHunterApi()
v.get_vacancies('репетитор')
print('--------------------------------')
a = SuperJob()
a.get_vacancies('репетитор')

class Vacancy:
    def __init__(self, name_vacancy, url_vacancy, work_experience, salary_from=None, salary_to=None):
        self.__name_vacancy = name_vacancy
        self.__url_vacancy = url_vacancy
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__experience = work_experience


