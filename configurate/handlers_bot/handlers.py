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
sys.path.append('config')
from configurate import *
sys.path.append('configurate/handlers_bot/functions')
import table
from info_goals import *
from eng_rus import *




async def creating_new_bot(message: types.Message):
    list_of_goals = types.InlineKeyboardMarkup(row_width=1)
    if await table.get_goals(message.from_user.id) != None:
        text_and_data = (await table.get_goals(message.from_user.id))
        all_goals = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
        list_of_goals.add(*all_goals)
        if await table.check_lang(message.from_user.id) == 'rus':
            await message.answer(choose_rus, reply_markup=list_of_goals)
        else:
            await message.answer(choose_eng, reply_markup=list_of_goals)
    else:
        if await table.check_lang(message.from_user.id) == 'rus':
            await message.answer(u_havent_rus)
        else:
            await message.answer(u_havent_eng)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(creating_new_bot, commands = 'goals')
