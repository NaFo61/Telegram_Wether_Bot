from loader import bot

from data.create_db import create_customer_table

from telebot import types
from telebot.types import Message

from states.mystates import MyStates

from funcs.func_with_db import get_users_name_from_users_id, get_users_spin_from_users_id, put_to_db, lose_one_spin
from funcs.func_with_api import get_information
from funcs.func_with_translate import get_translate

from texts.texts import TODAY_WEATHER, START_MESSAGE, MESSAGE_START, MESSAGE_HELP, MESSAGE_QUESTION

my_state = MyStates()


@bot.message_handler(commands=['start'])  # Декоратор, который реагирует на команду start
def start(message: Message):
    put_to_db(message.from_user.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем сетку для главных кнопочек
    item1 = types.KeyboardButton(
        'Получить бесплатный прозноз погоды на сегодня')  # Создаем кнопочку
    item2 = types.KeyboardButton('Вопрос/Ответ')  # Создаем кнопочку
    item3 = types.KeyboardButton('Регистрация')  # Создаем кнопочку
    markup.add(item1)
    markup.add(item2, item3)
    mes = MESSAGE_START.format(name_user=message.from_user.first_name)
    bot.send_message(message.chat.id, mes, reply_markup=markup)


@bot.message_handler(commands=['help'])  # Декоратор, который реагирует на команду help
def help(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем сетку для главных кнопочек
    item1 = types.KeyboardButton(
        'Начать использовать')  # Создаем кнопочку
    item2 = types.KeyboardButton('Вопрос/Ответ')  # Создаем кнопочку
    markup.add(item1)
    markup.add(item2)
    mes = MESSAGE_HELP
    bot.send_message(message.chat.id, mes, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def run(message: Message):
    user_message = message.text  # Получаем значение, которое отправил пользователь
    if user_message == 'Получить бесплатный прозноз погоды на сегодня':
        if my_state.free_spin:
            count_of_spin = get_users_spin_from_users_id(message.from_user.id)
            print(count_of_spin)
            if count_of_spin > 0:
                bot.send_message(message.chat.id, 'Напиши свой город')
                my_state.write_city = True
            else:
                bot.send_message(message.chat.id, 'Не хватате спинов')
    elif user_message == 'Вопрос/Ответ':
        question_answer(message)
    elif user_message == 'Регистрация':
        result = get_users_name_from_users_id(message.from_user.id)
        if not result:
            bot.send_message(message.chat.id, 'Введи свое имя')
            my_state.write_name = True
        else:
            bot.send_message(message.chat.id, 'Вы уже зареганы')
    elif user_message == 'Начать использовать':
        start(message)
    else:
        if my_state.write_city:
            my_state.write_city = False
            my_state.city = user_message

            count_of_spin = get_users_spin_from_users_id(message.from_user.id)
            if count_of_spin > 0:
                lose_one_spin(message.from_user.id)
                get_forecast_today(message)
        elif my_state.write_name:
            my_state.write_name = False
            result = put_to_db(message.from_user.id, user_message, registration=True)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, 'Иди нафиг, я от тебя ничего не жду')


def get_forecast_today(message: Message):
    try:
        dct_information = get_information(my_state.city)
        type_of_weather = dct_information.get('type_of_weather', 'Error')
        today_day = dct_information.get('today_day', 'Error')
        altimetr = dct_information.get('altimetr', 'Error')
        snow_detect = dct_information.get('snow_detect', 'Error')
        sun_rise = dct_information.get('sun_rise', 'Error')
        sun_set = dct_information.get('sun_set', 'Error')
        temperature = dct_information.get('temperature', 'Error')
        temperature_feel = dct_information.get('temperature_feel', 'Error')
        temperature_max = dct_information.get('temperature_max', 'Error')
        temperature_min = dct_information.get('temperature_min', 'Error')
        wind_speed = dct_information.get('wind_speed', 'Error')

        today_day = get_translate(today_day)
        type_of_weather = get_translate(type_of_weather)

        RESULT = TODAY_WEATHER.format(
            type_of_weather=type_of_weather,
            today_day=today_day,
            altimetr=altimetr,
            snow_detect=snow_detect,
            sun_rise=sun_rise,
            sun_set=sun_set,
            temperature=temperature,
            temperature_feel=temperature_feel,
            temperature_max=temperature_max,
            temperature_min=temperature_min,
            wind_speed=wind_speed)

        bot.send_message(message.chat.id, RESULT)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Ошибка, попробуй еще раз')
        my_state.write_city = True


def question_answer(message: Message):
    bot.send_message(message.chat.id, MESSAGE_QUESTION)



if __name__ == '__main__':
    print(START_MESSAGE)
    create_customer_table()
    bot.polling(none_stop=True)
