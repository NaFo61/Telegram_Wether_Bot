from telebot.handler_backends import State, StatesGroup

class MyStates(StatesGroup):
    free_spin = State()
    city = State()
    write_city = State()
    name = State()
    write_name = State()