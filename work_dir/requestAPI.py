from abc import ABC, abstractmethod
import requests
import os
from datetime import datetime


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    """Данный класс создает запрос на API hh.ru"""

    def get_request(self):
        vacancy_list = []
        for item in range(25):
            request = requests.get("https://api.hh.ru/vacancies?text=Python developer",
                                   params={'page': item, "experience": "noExperience"}).json()['items']
            for item2 in request:
                vacancy_list.append(item2)
        return vacancy_list


class SuperJob(Engine):
    """Данный класс создает запрос на API Superjob.ru"""

    def get_request(self):
        vacancy_list = []
        my_auth_data = {"X-Api-App-Id": os.environ['SUPERJOB_API_KEY']}  # Ключ(Токен)
        for item in range(25):
            request = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                   headers=my_auth_data,
                                   params={"keywords": "Python developer", "page": item}).json()['objects']
            for item2 in request:
                vacancy_list.append(item2)
        return vacancy_list


class HHVacancy():
    """ HeadHunter Vacancy """

    def __init__(self, data):
        self.data = data
        self.profession = self.data[0]['name']  # Название вакансии
        self.url = self.data[0]['apply_alternate_url']  # Ссылка на вакансию
        self.description = self.data[0]["snippet"]['responsibility']  # Описание вакансии
        self.payment = f"от {self.data[0]['salary']['from']} до {self.data[0]['salary']['to']}"  # Зарплата от и до

    def get_info_vacancy(self):
        """ Метод выводит сайт, названи, ссылку, зарплатную вилку,
            и время размещение вакансий """
        lis_vacansy = []
        for item in self.data:
            info = {
                'source': "HeadHunter",
                'name': item['name'],
                'url': item['alternate_url'],
                'salary': {
                    'from': None if item["salary"] == None else item["salary"]["from"],
                    'to': None if item["salary"] == None else item["salary"]["to"]},
                'date_published': datetime.strptime(item['published_at'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d'),
            }
            lis_vacansy.append(info)
        return lis_vacansy

    def get_count_of_vacancy(self):
        """
        Вернёт количество вакансий от текущего сервиса.
        """
        return len(self.data)

    def __repr__(self):
        return f'HH(Example):\nProfession: {self.profession}\n' \
               f'Зарплата: {self.payment} руб/мес'


class SJVacancy():
    """ SuperJob Vacancy """

    def __init__(self, data):
        self.data = data
        self.profession = self.data[0]['profession']  # Название вакансии
        self.url = self.data[0]['link']  # Ссылка на вакансию
        self.description = self.data[0]['candidat']  # Описание вакансии
        self.payment = f"от {self.data[0]['payment_from']} до {self.data[0]['payment_to']}"  # Зарплата от и до

    def get_info_vacancy(self):
        """ Метод выводит сайт, названи, ссылку, зарплатную вилку,
            и время размещение вакансий """
        lis_vacansy = []
        for item in self.data:
            info = {
                'source': "SuperJob",
                'name': item['profession'],
                'url': item['link'],
                'salary': {'from': None if item["payment_from"] == 0 else item["payment_from"],
                           'to': None if item["payment_to"] == 0 else item["payment_to"]},
                'date_published': datetime.utcfromtimestamp(item['date_published']).strftime('%Y-%m-%d')
            }
            lis_vacansy.append(info)
        return lis_vacansy

    def get_count_of_vacancy(self):
        """
        Вернёт количество вакансий от текущего сервиса.
        """
        return len(self.data)

    def __repr__(self):
        return f'SuperJob(Example):\nProfession: {self.profession}\n' \
               f'Зарплата: {self.payment} руб/мес'


def union(lis, lis2):
    """Функция объеденят два запроса с сайтов в один список"""
    list_all_vacansy = []
    for item in lis:
        list_all_vacansy.append(item)
    for item in lis2:
        list_all_vacansy.append(item)
    return list_all_vacansy
