# HW6 Logutov
1. БД MySQL находится в контейнере Docker, запущенном локально.
2. Работа с БД реализована с использованием sqlalchemy
3. Код для обработки 2, 3 и 5 заданий взят из HW5
4. 1 и 4 задания мокнуты (1 просто хардкод, 4 берется из top5_4xx.log в /data) в соответствии с рекомендацией
5. Исходный лог-файл access.log должен находиться в /data
6. В ассертах проверяется не просто количество записей в таблице БД, а сравнивается содержимое

## Запуск
* Тесты работают в многопоточном режиме (xdist)
* Команда для запуска: **pytest -n=4**
* Команда для развёртывания БД **docker run --name TEST_SQL -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass -d mysql:8.0**"
