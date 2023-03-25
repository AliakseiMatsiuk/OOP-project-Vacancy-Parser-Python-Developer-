from requestAPI import HH, SuperJob, HHVacancy, SJVacancy, union
from pprint import pprint
from datetime import datetime
import json


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    """
    data_file = None

    def __init__(self, file):
        self.file = file


    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        try:
            with open(self.file, "r") as f:
                json.load(f)
        except FileNotFoundError:
            with open(self.file, "w") as f:
                json.dump([], f)
        except json.JSONDecodeError:
            raise Exception("Файл поврежден")

    def insert(self):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        data = json.dumps(self.file)
        data = json.loads(str(data))
        with open('vacans.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def select_by_salary(self, salary_min, salary_max):
        """
        Выбор данных из файла с применением фильтрации
        по диапазону  зарплаты
        """
        try:
            with open("vacans.json", 'r') as f:
                data = json.load(f)
        except Exception:
            print("Файл пустой, запишите данные в файл!")
            return []

        filtered_data = []
        for vacancy in data:
            salary = vacancy['salary']
            if salary['from'] is None:
                salary_from = 0
            else:
                salary_from = salary['from']
            if salary['to'] is None:
                salary_to = float('inf')
            else:
                salary_to = salary['to']
            if salary_from >= salary_min and salary_to <= salary_max:
                filtered_data.append(vacancy)
        return filtered_data

    def jobs_by_date(self, num_jobs, date_str):
        """ Метод сортирует по количеству вакансий и по дате """
        try:
            with open('vacans.json', 'r') as f:
                job_data = json.load(f)
        except Exception:
            print("Файл пустой, запишите данные в файл!")
            return []

        dt = datetime.strptime(date_str, "%Y-%m-%d").date()

        jobs = [job for job in job_data if datetime.strptime(job['date_published'], "%Y-%m-%d").date() == dt]
        vacansy = []
        for job in jobs[:num_jobs]:
            vacansy.append(job)
        return vacansy


    def delete(self):
        """
        Удаление всех записей из файла.
        """
        open("vacans.json", "w").close()

    def read(self):
        """Читает содержимое файла и выводит на экран"""
        try:
            with open('vacans.json', 'r') as f:
                job_data = json.load(f)
                return job_data
        except Exception:
            print("Файл пустой, запишите данные в файл!")
            return []

    def type_of_vacancies(self, jobs):
        for job in jobs:
            print(f"Дата публикации: {job['date_published']}\n"
                  f"Название вакансии: {job['name']}\n"
                  f"Зарплата: от - {job['salary']['to']} до - {job['salary']['to']}\n"
                  f"Ресурс: {job['source']}\n"
                  f"URL : {job['url']}")
            print()

