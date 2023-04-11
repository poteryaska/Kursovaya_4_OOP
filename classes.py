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

    def get_vacancies(self, surch_text):
        params = {"text": surch_text}
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

    def get_vacancies(self, surch_text):
        api_key = {'X-Api-App-Id': 'v3.h.4455282.7eb36007ef58eb15c52a61399870fe45fa6e854d.1fda0d61019317af27f3361fe0d54e6e149fef37'}
        params = {"keyword": surch_text}
        response = requests.get(self.__url, headers=api_key, params=params)
        if response.status_code == 200:
            vacancies = response.json()["objects"]
            with open("vacancies_SJ.json", "w", encoding='utf-8') as write_file:
                json.dump(vacancies, write_file, indent=4, ensure_ascii=False)
            for vacancy in vacancies:
                print(vacancy["profession"], vacancy["link"])
        else:
            print("Error:", response.status_code)

v = HeadHunterApi()
v.get_vacancies('репетитор')
print('--------------------------------')
a = SuperJob()
a.get_vacancies('репетитор')
