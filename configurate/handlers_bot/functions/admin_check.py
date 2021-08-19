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

from config import TOKEN
from __main__ import *

async def is_adminn(userid):
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users where id = ?"""

    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchall()
    for row in records:
        if row[2] == 'admin':
            return True
            break
        else:
            return False
