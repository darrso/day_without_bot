import sys
import os
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
from config import *
import table
from info_goals import *
from eng_rus import *
class CreatingNewGoal(StatesGroup):
    CreatingNew_1 = State()
    CreatingNew_2 = State()

async def creating_new_1(message: types.Message, state:FSMContext):
    if await table.check_lang(message.from_user.id) == 'rus':
        await message.answer(new_rus)
    else:
        await message.answer(new_eng)
    await CreatingNewGoal.CreatingNew_1.set()


async def creating_new_2(message: types.Message, state:FSMContext):
    if await table.adding_new_goal(message.text.lower(), message.from_user.id) == True:
        data = message.text.lower()
        if await table.check_lang(message.from_user.id) == 'rus':
            await message.answer(f'🍃Новая цель создана!\n🐲Вы хотите начать жить без {data}\n\n🔅Для просмотра своих целей введите /goals')
        else:
            await message.answer(f'🍃A new goal has been created!\n🐲You want to start to live without {data}\n\n🔅To check your goals - /goals')
    else:
        if await table.check_lang(message.from_user.id) == 'rus':
            await message.answer(three_goals_rus)
        else:
            await message.answer(three_goals_eng)
    await state.finish()

class One_Goal(StatesGroup):
    One_Goal_1 = State()
    One_Goal_2 = State()

async def choose_from_goals(query: types.CallbackQuery, state:FSMContext):
    answer_data = query.data
    await state.update_data(number=answer_data)
    text = await goal_number_1(query.from_user.id, answer_data)
    date = await get_date(query.from_user.id, answer_data)
    count = await get_count(query.from_user.id, answer_data)
    list_of_goal = types.InlineKeyboardMarkup(row_width = 3)
    if await table.check_lang(query.from_user.id) == 'rus':
        text_and_data = (
            ('✅Отметиться✅', 'new_day'), ('❌Удалить цель❌', 'delete')
        )
    else:
        text_and_data = (
            ('✅Check in✅', 'new_day'), ('❌Delete goal❌', 'delete')
        )
    one_goal = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    list_of_goal.add(*one_goal)
    if await table.check_lang(query.from_user.id) == 'rus':
        list_of_goal.add(types.InlineKeyboardButton(text="🌄Сгенерировать изображение🌄", callback_data="generate"))
    else:
        list_of_goal.add(types.InlineKeyboardButton(text="🌄Generate Image🌄", callback_data="generate"))
    if await table.check_lang(query.from_user.id) == 'rus':
        await bot.send_message(query.from_user.id, f'🎾Жизнь без {text}🎾\n\n'
            f'🍿Дата начала - {date}\n'
            f'🍿Количество дней - {count}', reply_markup=list_of_goal)
    else:
        await bot.send_message(query.from_user.id, f'🎾Life without {text}🎾\n\n'
            f'🍿The date of the beginning - {date}\n'
            f'🍿Number of days - {count}', reply_markup=list_of_goal)
    await One_Goal.One_Goal_1.set()


async def new_and_delete(query: types.CallbackQuery, state:FSMContext):
    if query.data == 'new_day':
        result = await new_day(query.from_user.id, await state.get_data())
        if (result == 'started') or (result == 'started_2'):
            if await table.check_lang(query.from_user.id) == 'rus':
                await query.answer(new_day_rus)
            else:
                await bot.send_message(query.from_user.id, new_day_eng)
        elif result == 'today':
            if await table.check_lang(query.from_user.id) == 'rus':
                await bot.send_message(query.from_user.id, go_tomorrow_rus)
            else:
                await bot.send_message(query.from_user.id, go_tomorrow_eng)
        elif result == 'sbiv':
            if await table.check_lang(query.from_user.id) == 'rus':
                await bot.send_message(query.from_user.id, sbiv_rus)
            else:
                await bot.send_message(query.from_user.id, sbiv_eng)
    elif query.data == 'delete':
        await delete_goal(query.from_user.id, await state.get_data())
        if await table.check_lang(query.from_user.id) == 'rus':
            await bot.send_message(query.from_user.id, deleted_rus)
        else:
            await bot.send_message(query.from_user.id, deleted_eng)
    elif query.data == 'generate':
        await bot.send_photo(query.from_user.id, photo = open(await generate_image(query.from_user.id, await state.get_data()), 'rb'))
        os.remove('new_img.jpg')
    await state.finish()

def register_handlers_states(dp: Dispatcher):
    dp.register_message_handler(creating_new_1, commands = 'new', state = None)
    dp.register_message_handler(creating_new_2, state = CreatingNewGoal.CreatingNew_1)
    dp.register_callback_query_handler(choose_from_goals, text=['1', '2', '3'], state = None)
    dp.register_callback_query_handler(new_and_delete, text = ['new_day', 'delete', 'generate'], state = One_Goal.One_Goal_1)