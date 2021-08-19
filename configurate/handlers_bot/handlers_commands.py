import sys
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from times import *
from emoji import  *

from config import *
import table
from info_goals import *
from eng_rus import *
from admin_check import *
from admin_panel import *
async def start_command_answer(message: types.Message):
    if message.text == '/start':
        await table.get_userid_username(message.from_user.id, message.from_user.username)
        if await table.check_lang(message.from_user.id) == 'rus':
            await message.answer(text = start_russian)
        else:
            await message.answer(text = start_eng)
    elif message.text == '/help':
        if await table.check_lang(message.from_user.id) == 'rus':
            await message.answer(help_rus)
        else:
            await message.answer(text = help_eng)
async def languages(message: types.Message):
    if message.text == '/english':
        await table.switch_to_eng(message.from_user.id, message)
        await message.answer(text = 'You have successfully changed the language.🥂')
    else:
        await table.switch_to_rus(message.from_user.id, message)
        await message.answer(text = 'Вы успешно сменили язык!🥂')

async def admin_panel(message: types.Message):
    if await is_adminn(message.from_user.id):
        await message.answer('🦾Вы находитесь в панеле админа.', reply_markup = admin_panel_bttns)

def register_handlers_commands(dp:Dispatcher):
    dp.register_message_handler(start_command_answer, commands=['start', 'help'])
    dp.register_message_handler(languages, commands = ['english', 'russian'])
    dp.register_message_handler(admin_panel, commands = 'admin')