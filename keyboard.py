from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder




rkb = ReplyKeyboardBuilder()

rkb.add(*[KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")])
rkb.add(*[KeyboardButton(text="Hodim kerak"), KeyboardButton(text="Ustoz kerak")])
rkb.add(KeyboardButton(text="Shogird kerak"))

rkb.adjust(2, repeat=True,)



ikb = InlineKeyboardBuilder()

ikb.add(
    InlineKeyboardButton(text="Ha", callback_data="confirm"),
    InlineKeyboardButton(text="Yoq", callback_data="reject")
)
