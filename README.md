# TelegramTODOList
Телеграм бот реализующий функционал всем известного листа заметок.

# Планы
---Ближайшие
1) Добавление инлайн-кнопок - подзадач
2) Возможность вывести список задач, которых нет в чате.
3) Добавить возможность создания задачи из аудио-сообщения.
4) Прикрутить статистику. Для начала - созданные/выполненные задачи

---Планы на развитие сервиса
1) Оптимизация запросов. Вдруг будет высокая нагрузка))
2) Добавить возможность создания задачи из аудио-сообщения. 
Возможность надиктовывать описание, менять даты.
3) Прикрутить Celery, которая бы вместо вычисляемого статуса по запросу, меняла бы его в базе данных в нон-стоп режиме.
4) Оповещения клиентов о изменении статуса поставленной задачи посредством Celery.


# Запуск
Для запуска необходим docker

Инструкция
1) Клонировать проект
2) Находясь в корне проекта - docker-compose build
3) Как билд закончится, обновить данные базы данных
4) Запуск по команде docker-compose up -d

* Команды для работы с докером
docker-compose ps - выведет список запущенных контейнеров
docker-compose logs <app> - выведет лог приложения <app>. Без аргумента - логи всех приложенией.
docker-compose exec <app> <command> - выполнить команду (как в терминале) для приложения <app>.
Например, узнать список установленных пакетов python 
docker-compose exec app pip list
