# Инструкция по запуску приложения через Docker

Для запуска приложения "New-Telegram" через Docker, выполните следующие шаги:

## Шаг 1: Установка Docker
Убедитесь, что вы установили Docker на ваш компьютер. Вы можете скачать и установить Docker с официального сайта Docker: [https://www.docker.com/get-started](https://www.docker.com/get-started)

## Шаг 2: Сборка образа Docker
1. Откройте терминал или командную строку и перейдите в папку проекта "New-Telegram".
2. Выполните команду docker build -t new-telegram . для сборки образа Docker. В этой команде мы использовали тег "new-telegram" для образа.

## Шаг 3: Запуск контейнера Docker
1. После успешной сборки образа Docker, выполните команду docker run -d -p 8000:8000 --name new-telegram-container new-telegram для запуска контейнера. В этой команде мы привязываем порт 8000 на хостовой машине к порту 8000 в контейнере, а также называем контейнер "new-telegram-container".
2. Ваше приложение "New-Telegram" теперь должно быть доступно на [http://localhost:8000](http://localhost:8000).

## Шаг 4: Остановка и удаление контейнера
Если вы хотите остановить и удалить контейнер Docker, выполните команды:
- docker stop new-telegram-container - остановит работу контейнера.
- docker rm new-telegram-container - удалит контейнер.
