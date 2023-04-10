from abc import ABC, abstractmethod
import requests
import json

url = "https://api.hh.ru/vacancies"
params = {
    "text": "python",
    "per_page": 100,
    "salary": 50000
}

response = requests.get(url, params=params)

if response.status_code == 200:
    vacancies = response.json()["items"]
    with open("vacancies.json", "w", encoding='utf-8') as write_file:
        json.dump(vacancies, write_file, indent=4, ensure_ascii=False)
    for vacancy in vacancies:
        print(vacancy["name"], vacancy["url"])
else:
    print("Error:", response.status_code)






class Job(ABC):
    @abstractmethod
    def connect_api(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

class HeadHunter(Job):
    pass

class SuperJob(Job):
    pass