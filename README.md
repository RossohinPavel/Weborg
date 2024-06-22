# Weborg
Веб-Органайзер для работы

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
