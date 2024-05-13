from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    button = ""
    full_name = State()
    age = State()
    technologies = State()
    phone_number = State()
    address = State()
    price = State()
    work_place = State()
    goal = State()