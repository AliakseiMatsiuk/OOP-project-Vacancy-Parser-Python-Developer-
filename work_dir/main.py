from connector import Connector
from requestAPI import HH, SuperJob, HHVacancy, SJVacancy, union
from pprint import pprint

print('Приветствую тебя пользователь.\n'
      'В данной програме мы сможем вывести для тебя 1000 вакансий Python developer\n'
      'по задваемым пораметрам с помощью нужных каманд из сайта Superjob и HeadHunter')
print()
input("Нажмите Enter чтобы подолжить")
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
      "count_vacansy - эта команда покажит колличество доступный вакансий;\n"
      "\n"
      "all_vacansy - команда выведит вообще все вакансии на экран\n"
      "\n"
      "salary_range - Где первая цыфра запроса это зарплата от-(1000), а втарая до-(2000) по вакансии\n"
      "\n"
      "data_range - эта команда сортирут по колличеству вакансий(10)\n"
      "и по запрашиваемой дате('2023-03-16')\n"
      "\n"
      "Exet - Если желаешь завершить работу\n"
      "Далее ты можешь попробывать вышестоящие команды в кансоле\n")
command = "count_vacansy - эта команда покажит колличество доступный вакансий;\n"\
          "all_vacansy - команда выведит вообще все вакансии на экран\n"\
          "salary_range - Где первая цыфра запроса это зарплата от-(1000), а втарая до-(2000) по вакансии;\n" \
          "data_range - эта команда сортирут по запрашиваемой дате('2023-03-16')\n"\
          "и по колличеству вакансий (10)\n" \
          "Exet - Завершить работу"
request = input()
while request != "Exet":
    if request == "count_vacansy":
        pprint(len(con.read()))
        print()
        request = input()
    elif request == "all_vacansy":
        pprint(con.read())
        print(command)
        request = input()
    elif request == "salary_range":
        fromm = input("Напиши со скольки ищишь зп ")
        to = input("Напиши до скольки ищишь зп ")
        if fromm.isdigit() and to.isdigit():
            pprint(con.select_by_salary(int(fromm), int(to)))
            print()
            print(command)
            request = input()
        else:
            print("Диапазон ЗП должен быть только в цыфровом виде")
    elif request == "data_range":
        amount = input("Напиши количество вакансий ")
        data= input("Напиши дату,например: 2023-03-16 ")
        if amount.isdigit() and data.replace("-", '').isdigit():
            pprint(con.jobs_by_date(int(amount), data))
            print()
            print(command)
            request = input()
        else:
            print("Что-то ты не то написал. Давай ещё раз!")
    else:
        print("Тут не таких команд!")
        request = input()

print("Вот и всё. Спасибо за то что воспользовались нашим сервисом.\n"
      "Оставте пожалуста свои отзовы у нас на сайте: 'https://tutortop.ru/school-reviews/skypro/'")
