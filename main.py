import asyncio
import json
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

t = '9077426533:AAE1Rynt8RDmrMmapnS1uENS86AX4Ta_O4E'

with open('knowledge.json', 'r', encoding='utf-8') as file:
    answers = json.load(file)

bot = Bot(token=t)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Травля'), KeyboardButton(text='Взлом')],
        [KeyboardButton(text='Мошенники'), KeyboardButton(text='Фишинг')],
        [KeyboardButton(text='Шантаж'), KeyboardButton(text='Незнакомцы')],
        [KeyboardButton(text='Игровая валюта'), KeyboardButton(text='Приватность')],
        [KeyboardButton(text='Школа'), KeyboardButton(text='Пароли')]
    ],
    resize_keyboard=True
)

@dp.message(F.text == '/start')
async def start(message: Message):
    await message.answer('Привет! Выбери тему на кнопках ниже или опиши свою ситуацию словами.', reply_markup=menu)

@dp.message(F.text)
async def get_answer(message: Message):
    text = message.text.lower()
    
    if text == 'травля' or 'травят' in text or 'обижают' in text or 'буллинг' in text or 'дразнят' in text:
        await message.answer(answers['travlya'])
    elif text == 'взлом' or 'взломали' in text or 'пароль' in text or 'аккаунт' in text:
        await message.answer(answers['vzlom'])
    elif text == 'мошенники' or 'обман' in text or 'деньги' in text or 'перевел' in text or 'карта' in text:
        await message.answer(answers['moshenniki'])
    elif text == 'фишинг' or 'ссылка' in text or 'перейти' in text:
        await message.answer(answers['fikshing'])
    elif text == 'шантаж' or 'угрожают' in text or 'фото' in text:
        await message.answer(answers['doksing'])
    elif text == 'незнакомцы' or 'незнакомый' in text or 'чужой' in text:
        await message.answer(answers['neznakomcy'])
    elif text == 'игровая валюта' or 'скины' in text or 'робукс' in text or 'roblox' in text:
        await message.answer(answers['igrovaya_valyuta'])
    elif text == 'приватность' or 'настройки' in text or 'профиль' in text:
        await message.answer(answers['nastroiki'])
    elif text == 'школа' or 'одноклассники' in text or 'класс' in text:
        await message.answer(answers['kiberbulling_shkola'])
    elif text == 'пароли' or 'надежный пароль' in text:
        await message.answer(answers['paroli'])
    elif text == 'безопасные ссылки' or 'куда нажать' in text:
        await message.answer(answers['bezopasnye_ssylki'])
    else:
        await message.answer('Я не знаю такой темы. Нажми на кнопку ниже.', reply_markup=menu)

async def main():
    print('КиберГид запущен. Ожидаю сообщения...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
