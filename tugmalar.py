from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Reply Keyboard
main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="1-tugma")
    ],
    [
        KeyboardButton(text="2-tugma"), 
        KeyboardButton(text="3-tugma")
    ],
    [
        KeyboardButton(text="4-tugma"), 
        KeyboardButton(text="5-tugma"), 
        KeyboardButton(text="6-tugma")
    ]
],
resize_keyboard=True,
input_field_placeholder="Kerakli tugmani bosing...")

# Inline Keyboard
settings = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Google", url="https://www.google.com/"), 
            InlineKeyboardButton(text="Yandex", url="https://www.ya.ru")
        ],    
        [
            InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/"), 
            InlineKeyboardButton(text="Github", url="https://www.github.com/"), 
            InlineKeyboardButton(text="MEGA", url="https://www.mega.nz/")
        ]
])



cars = ['Nexia 2', 'Gentra', 'Damas', 'Cobalt', 'Malibu', 'Tahoe']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://www.uzautomotors.com/'))
    return keyboard.adjust(3).as_markup()



# Uyga vazifa: Unikal mavzuda Bot yarating, unda 10 ta Handler yarating, ularning har birida 10 tadan tugma bo'lsin!

# Statik
# 2 ta Handler Reply keyboard orqali yaratilsin!
# 3 ta Handler Inline keyboard orqali yaratilsin!

# Dinamik
# 5 ta Handlerda for orqali button bo'lsin!
# 2 ta Handler Reply keyboard orqali yaratilsin!
# 3 ta Handler Inline keyboard orqali yaratilsin!
