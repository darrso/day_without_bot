import sqlite3
import sys
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import emoji
from time import *
from __main__ import *
from config import TOKEN
from buttons import *

async def how_much_users():
    conn = sqlite3.connect('table.db')
    c = conn.cursor()

    c.execute("""SELECT * from users""")
    a = len(c.fetchall())
    return a
async def all_users():
    conn = sqlite3.connect('table.db')
    c = conn.cursor()

    c.execute("""SELECT * from users""")
    records = c.fetchall()

    all_message = ''
    for row in records:
        all_message += '\n' + str(row[0]) +'> '+ row[1] + ' | '+ row[2]
    return all_message
class Mailing(StatesGroup):
            Mailing_1 = State()
            Mailing_2 = State()

async def count_and_mailing(query: types.CallbackQuery, state:FSMContext):
    if query.data == 'count':
        count = await how_much_users()
        await bot.send_message(query.from_user.id, f'🍿Количество зарегестрированных пользователей - {count}')
    elif query.data == 'mailing':
        await bot.send_message(query.from_user.id, 'Введите текст рассылки(или "Отмена" для ее отмены):')
        await Mailing.Mailing_1.set()
    elif query.data == 'spisok':
        spisok = await all_users()
        await bot.send_message(query.from_user.id, f'🍿Список пользователей:\n\n{spisok}')

async def mailing_contunue(message: types.Message, state:FSMContext):
    if message.text != 'Отмена':
        conn = sqlite3.connect('table.db')
        c = conn.cursor()

        c.execute("""SELECT * from users""")
        records = c.fetchall()
        for row in records:
            await bot.send_message(chat_id=row[0], text=message.text)
            sleep(0.3)

        await message.answer('Рассылка была разослана')
        await message.answer('🦾Вы находитесь в панеле админа.', reply_markup = admin_panel_bttns)
    else:
        await message.reply('Вы отменили рассылку.')
        await message.answer('🦾Вы находитесь в панеле админа.', reply_markup = admin_panel_bttns)
    await state.finish()

def register_handlers_adm(dp:Dispatcher):
    dp.register_callback_query_handler(count_and_mailing, text = ['count', 'mailing', 'spisok'], state = None)
    dp.register_message_handler(mailing_contunue, state = Mailing.Mailing_1)