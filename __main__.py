import sys
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configurate import *

from configurate.handlers_bot.handlers import *
from handlers_bot.handlers_commands import *
from handlers_bot.handlers_states import *
from handlers_bot.functions.admin_panel import *
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage()) #--BOT--


    register_handlers(dp)
    register_handlers_commands(dp)
    register_handlers_states(dp)
    register_handlers_adm(dp)
    await dp.start_polling()





if __name__ == '__main__':
    asyncio.run(main())
