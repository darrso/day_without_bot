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

#КНОПКИ АДМИН ПАНЕЛИ
admin_panel_bttns = types.InlineKeyboardMarkup(row_width=3)
text_and_data = (
        ('Кол-во пользователей', 'count'), ('Рассылка', 'mailing'), ('Список всех пользователей', 'spisok')
    )
all_bttns_adm_panel = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
admin_panel_bttns.add(*all_bttns_adm_panel)