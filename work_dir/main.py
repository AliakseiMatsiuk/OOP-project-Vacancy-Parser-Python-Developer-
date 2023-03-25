from connector import Connector
from requestAPI import HH, SuperJob, HHVacancy, SJVacancy, union
from pprint import pprint

print('Приветствую тебя пользователь.\n'
      'В данной программе мы сможем вывести для тебя 1000 вакансий Python developer\n'
      'по задаваемым параметрам с помощью нужных команд из сайта Superjob и HeadHunter')
print()
input("Нажмите Enter чтобы продолжить")

hh = HH().get_request()
sj = SuperJob().get_request()
sjvacasy = SJVacancy(sj)
hhvacasy = HHVacancy(hh)
con = Connector(union(sjvacasy.get_info_vacancy(), hhvacasy.get_info_vacancy()))
con.insert()

print()
print("На данном этапе сделан запрос на сервер и информация по вакансиям\n"
      "записана в JSON файл")
print()

print("Теперь доступны команды:\n"
      "\n"
      "count_vacansy - эта команда покажет количество доступный вакансий;\n"
      "\n"
      "all_vacansy - команда выведет вообще все вакансии на экран\n"
      "\n"
      "salary_range - Где первая цифра запроса это зарплата от-(1000), а вторая до-(2000) по вакансии\n"
      "\n"
      "data_range - эта команда сортирует по количеству вакансий(10)\n"
      "и по запрашиваемой дате('2023-03-16')\n"
      "\n"
      "Exet - Если желаешь завершить работу\n"
      "Далее ты можешь попробовать вышестоящие команды в консоли\n")

command = "count_vacansy - эта команда покажет количество доступный вакансий;\n" \
          "all_vacansy - команда выведет вообще все вакансии на экран\n" \
          "salary_range - Где первая цифра запроса это зарплата от-(1000), а вторая до-(2000) по вакансии;\n" \
          "data_range - эта команда сортирует по запрашиваемой дате. Это формат ввода даты:'2023-03-16'\n" \
          "и по количеству вакансий (10)\n" \
          "Exet - Завершить работу"


def working_environment():
    request = input()

    while request != "Exet":

        if request == "count_vacansy":
            pprint(len(con.read()))
            print()
            request = input()

        elif request == "all_vacansy":
            con.type_of_vacancies(con.read())
            print(command)
            request = input()

        elif request == "salary_range":
            fromm = input("Напиши со скольки ищешь зп ")
            to = input("Напиши до скольки ищешь зп ")

            if fromm.isdigit() and to.isdigit():
                print()
                con.type_of_vacancies(con.select_by_salary(int(fromm), int(to)))
                print()
                print(command)
                request = input()
            else:
                print("Диапазон ЗП должен быть только в цифровом  виде")

        elif request == "data_range":
            amount = input("Напиши количество вакансий ")
            data = input("Напиши дату в формат ввода даты, например: 2023-03-16 ")

            if amount.isdigit() and data.replace("-", '').isdigit():
                print()
                con.type_of_vacancies(con.jobs_by_date(int(amount), data))
                print()
                print(command)
                request = input()
            else:
                print("Что-то ты не то написал. Давай ещё раз!")

        else:
            print("Тут нет таких команд!")
            request = input()


working_environment()

print("Вот и всё. Спасибо за то что воспользовались нашим сервисом.\n"
      "Оставьте, пожалуйста, свои отзывы у нас на сайте: 'https://tutortop.ru/school-reviews/skypro/'")
