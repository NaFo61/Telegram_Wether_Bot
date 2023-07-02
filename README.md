# Телеграм-бот для прогноза погоды

Добро пожаловать в репозиторий телеграм-бота, который предоставляет актуальный прогноз погоды для заданного города. Этот
бот использует открытое API для получения данных о погоде и позволяет пользователям легко получать информацию о погодных
условиях в любом городе.

## Установка и настройка

### Требования

Перед началом установки убедитесь, что у вас установлены следующие компоненты:

- Python 3 (https://www.python.org/downloads/)
- pip (устанавливается автоматически вместе с Python 3)

### Установка

1. Клонируйте репозиторий на свой компьютер:

git clone https://gitlab.skillbox.ru/stanislav_eliseev_1/python_basic_diploma

2. Перейдите в директорию проекта:

cd Telegram_Wether_Bot

3. Установите зависимости, указанные в файле requirements.txt:

pip install -r requirements.txt

### Настройка API-ключа

Для использования API прогноза погоды вам понадобится API-ключ. Вы можете получить его, зарегистрировавшись на
соответствующем веб-сервисе прогноза погоды. После получения ключа, сохраните его в файле `.env` в корневой папке
проекта. Создайте файл `.env` и добавьте в него следующую строку:

API_KEY=your-api-key

Замените `your-api-key` на ваш собственный API-ключ.

### Запуск бота

После завершения установки и настройки, вы можете запустить телеграм-бота:

python bot.py

## Использование

Откройте приложение Telegram и найдите бота по его имени или создайте нового бота, если у вас его еще нет.

Начните диалог с ботом, нажав кнопку "Старт" или отправив ему команду /start.

Введите название города, для которого вы хотите получить прогноз погоды. Например, Москва или London.

Бот отправит вам подробный прогноз погоды для заданного города, включая текущую температуру, влажность, скорость ветра,
а также прогноз на ближайшие дни.

Обратите внимание, что бот предоставляет один бесплатный прогноз погоды. Для получения дополнительных прогнозов
необходимо зарегистрироваться на этом же телеграм-боте.

Для регистрации нажмите на кнопку "Регистрация" в диалоге с ботом.

Введите всю необходимую информацию, которую спрашивает у вас бот.

Чтобы добавить API-ключ в настройки бота, отправьте команду /settings и следуйте инструкциям. После успешной настройки
ключа, вы сможете получать дополнительные прогнозы погоды.

Пользуйтесь ботом и наслаждайтесь удобным доступом к прогнозу погоды в любом городе!

## Вклад

Если вы хотите внести свой вклад в развитие этого проекта, вы можете создать pull request или сообщить об ошибках через
систему Issues. Все ваши предложения и вопросы приветствуются!

## Авторы

- Имя автора 1 - https://github.com/Elisey27-rus

## Благодарности

Мы хотели бы выразить благодарность следующим проектам и сообществам за их вклад в разработку этого бота:

- [Python](https://www.python.org/) - Отличный язык программирования.
- [python-telegram-bot](https://python-telegram-bot.org/) - Python-библиотека для работы с Telegram Bot API.
- [RapidApi](https://rapidapi.com/apidojo/api/weather338/) - Сервис прогноза погоды.

Мы также признательны всем нашим пользователям за их поддержку и обратную связь. Без вас этот проект не был бы возможен!
