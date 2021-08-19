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
from times import *
sys.path.append('configurate')
from config import *
from __main__ import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

async def get_userid_username(userid, username): #ВНЕСТИ В БД ДАННЫЕ ЮЗЕРА, НАПИСАВШЕГО /start
    conn = sqlite3.connect('table.db')
    c = conn.cursor()

    data = [userid, username, 'user', 'rus']
    c.execute('INSERT INTO users VALUES(?, ?, ?, ?)', data)
    conn.commit()

async def switch_to_eng(userid, message): #СМЕНА ЯЗЫКА НА АНГЛИЙСКИЙ
    conn = sqlite3.connect('table.db')
    c = conn.cursor()

    data = ('eng', userid)

    sqlee = """Update users set lang = ? where id = ?"""
    c.execute(sqlee, data)
    conn.commit()
    c.close()
async def switch_to_rus(userid, message): #СМЕНА ЯЗЫКА НА РУССКИЙ
    conn = sqlite3.connect('table.db')
    c = conn.cursor()

    data = ('rus', userid)
    
    sqlee = """Update users set lang = ? where id = ?"""
    c.execute(sqlee, data)
    conn.commit()
    c.close()

async def check_lang(userid): #ПРОВЕРКА ЯЗЫКА
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users where id = ?"""
    c.execute(sqlite_select_query, (userid, ))

    records = c.fetchall()
    for row in records:
        return row[3]

async def adding_new_goal(message, userid): #СОЗДАНИЕ НОВОЙ ЦЕЛИ
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    data = [userid, message]
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchone()
    count = -1
    try:
        for row in records:
            if row is None:
                continue
            else:
                count += 1
    except:
        pass
    data = ((message + '\n' + str(now().date())) + '\n0' + '\nNone', userid)
    if count == -1:
        sqlite_select_query = "INSERT INTO users_goals VALUES(?, ?, ?, ?)"
        data = (userid, (message + '\n' + str(now().date())) + '\n0' + '\nNone', None, None)
        c.execute(sqlite_select_query, data)
        conn.commit()
        c.close()
        return True
    elif (count >-1) and (count <3):
        sqlite_select_query = """Update users_goals set goal"""+str(count+1)+""" = ? where id = ?"""
        c.execute(sqlite_select_query, data)
        conn.commit()
        c.close()
        return True
    else:
        return False
async def get_goals(userid): #ПОЛУЧИТЬ СПИСОК ЦЕЛЕЙ
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchone()
    b = []
    try:
        for row in range(1, len(records)):
            if records[row] != None:
                a = records[row].split('\n')[0]
                b.append([str(a), str(row)])
        return (b)
    except:
        return None