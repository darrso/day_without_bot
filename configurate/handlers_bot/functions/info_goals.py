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
import emoji
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from times import *
from PIL import Image, ImageDraw, ImageFont
from config import *
from table import *
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

async def goal_number_1(userid, datanswer):
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchone()
    goal = records[int(datanswer)].split('\n')[0]
    return goal

async def get_date(userid, datanswer):
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchone()
    goal = records[int(datanswer)].split('\n')[1]
    return goal

async def get_count(userid, datanswer):
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchone()
    count = records[int(datanswer)].split('\n')[2]
    return count

async def new_day(userid, number):
    number_of_goal = number['number']
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchone()
    last_check = records[int(number_of_goal)].split('\n')[3]
    a = str(now().date()).split('-')[0]
    b = str(now().date()).split('-')[1]
    c = str(int(str(now().date()).split('-')[2]) - 1)
    a = f'{a}-{b}-{c}'
    text = str(records[int(number_of_goal)].split('\n')[0] + '\n' + records[int(number_of_goal)].split('\n')[1] + '\n' + str(int(records[int(number_of_goal)].split('\n')[2]) + 1) + '\n')
    if last_check == 'None':
        sqlite_select_query = """Update users_goals set goal"""+str(number_of_goal)+""" = ? where id = ?"""
        data = (text + str(now().date()), userid)
        conn = sqlite3.connect('table.db')
        c = conn.cursor()
        c.execute(sqlite_select_query, data)
        conn.commit()
        c.close()
        return 'started'

    elif last_check == a:
        sqlite_select_query = """Update users_goals set goal"""+str(number_of_goal)+""" = ? where id = ?"""
        data = (text + str(now().date()), userid)
        conn = sqlite3.connect('table.db')
        c = conn.cursor()
        c.execute(sqlite_select_query, data)
        conn.commit()
        c.close()
        return 'started_2'
    elif last_check == str(now().date()):
        return 'today'
    else:
        text = str(records[int(number_of_goal)].split('\n')[0] + '\n' + records[int(number_of_goal)].split('\n')[1] + '\n' + str(1) + '\n')
        sqlite_select_query = """Update users_goals set goal"""+str(number_of_goal)+""" = ? where id = ?"""
        data = (text + str(now().date()), userid)
        conn = sqlite3.connect('table.db')
        c = conn.cursor()
        c.execute(sqlite_select_query, data)
        conn.commit()
        c.close()
        return 'sbiv'
        
        
async def delete_goal(userid, number):
    number_of_goal = number['number']
    sqlite_select_query = """Update users_goals set goal"""+str(number_of_goal)+""" = ? where id = ?"""
    data = (None, userid)
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    c.execute(sqlite_select_query, data)
    conn.commit()
    c.close()
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchall()
    if number_of_goal == '1':
        for row in records:
            a = row[2]
            b = row[3]
    elif number_of_goal == '2':
        for row in records:
            a = row[1]
            b = row[3]
    sqlite_select_query = """Update users_goals set goal1 = ? where id = ?"""
    sqlite_select_query_2 = """Update users_goals set goal2 = ? where id = ?"""
    sqlite_select_query_3 = """Update users_goals set goal3 = ? where id = ?"""
    data = (a, userid)
    data_2 = (b, userid)
    data_3 = (None, userid)
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    c.execute(sqlite_select_query, data)
    c.execute(sqlite_select_query_2, data_2)
    c.execute(sqlite_select_query_3, data_3)
    conn.commit()
    if (a == None) and (b == None):
        deletee = """DELETE FROM users_goals WHERE id = ?"""
        c.execute(deletee, (userid, ))
    conn.commit()
    c.close()


async def generate_image(userid, number):
    conn = sqlite3.connect('table.db')
    c = conn.cursor()
    sqlite_select_query = """SELECT * from users_goals where id = ?"""
    c.execute(sqlite_select_query, (userid, ))
    records = c.fetchone()
    count = records[int(number['number'])].split('\n')[2]
    name = records[int(number['number'])].split('\n')[0]
    a = ['#DABDAB', '#BADBAD', '#A3C6C0', '#C8A2C8', '#A1A3C4']
    im = Image.new('RGB', (900,600), color = (random.choice(a)))
    watermark = Image.open('icon/logo.png')
    position = (im.width - watermark.width,
    im. height - watermark.height)
    im.paste(watermark, position, watermark)
    drow_text = ImageDraw.Draw(im)\

    slovo = (int(count) % 100)
    if slovo == 1:
        if await check_lang(userid) == 'rus':
            slovo_1 = 'день'
        else:
            slovo_1 = 'day'
    elif (slovo >= 2) and (slovo <=4):
        if await check_lang(userid) == 'rus':
            slovo_1 = 'дня'
        else:
            slovo_1 = 'days'
    else:
        if await check_lang(userid) == 'rus':
            slovo_1 = 'дней'
        else:
            slovo_1 = 'days'

    if await check_lang(userid) == 'rus':
        text = f'Я живу без {name}\n'
        text_2 = f'{count} {slovo_1}'
    else:
        text = f'I live without {name}\n'
        text_2 = f'{count} {slovo_1}'
    font = ImageFont.truetype('Dobrozrachniy-Regular.ttf', size=90, encoding='UTF-8')
    size_1_1, size_1_2 = drow_text.textsize(text, font = font)
    size_2_1, size_2_2 = drow_text.textsize(text_2, font = font)
    drow_text.text(
    ((900-size_1_1)/2,(600-size_1_2)/2),
    text,
    font=font,
    fill="black"
    )
    drow_text.text(
    ((850-size_2_1)/2,(650 -size_2_2)/2),
    text_2,
    font=font,
    fill="black"
    )
        
    im.save('new_img.jpg')
    return 'new_img.jpg'

