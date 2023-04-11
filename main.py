import requests
import json
api_key = {'X-Api-App-Id': 'v3.h.4455282.7eb36007ef58eb15c52a61399870fe45fa6e854d.1fda0d61019317af27f3361fe0d54e6e149fef37'}
        # params = {}
        # params['keyword'] = surch_text

params = {"keyword": 'python'}
response = requests.get(url, headers=api_key, params=params)
if response.status_code == 200:
    vacancies = response.json()["objects"]
    with open("vacancies_SJ.json", "w", encoding='utf-8') as write_file:
        json.dump(vacancies, write_file, indent=4, ensure_ascii=False)
    for vacancy in vacancies:
        print(vacancy["profession"], vacancy["link"])
else:
    print("Error:", response.status_code)