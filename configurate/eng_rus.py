from __main__ import *
start_russian = ('📨Привет! Я готов помочь вести тебе счет дней без чего-либо!\n'
                '🟡Напиши /help для того, чтоб разобраться в работе бота.\n\n'
                '🍿To switch to English, write /english . \n🍿In order to return to Russian - /russian .')

start_eng = ("📨Hi! I'm ready to help you keep track of the days without anything!\n\n"
                "🟡Write /help in order to understand the work of the bot.\n")

help_rus = ('🌱Создать новую цель - /new\n'
                'Максимальное количество целей, которые можно создать - 3\n\n'
                '🌿Посмотреть список своих целей - /goals\n'
                'Вы сможете посмотреть список активных целей, выбрать любую и отметить новый день ее достижения.\n\n'
                '🍿Сменить язык на английский - /english\n\n'
                '🍿Вернуть русский язык - /russian')
help_eng = ('🌱Create new goal - /new\n'
                'The maximum number of goals that can be created - 3\n\n'
                '🌿List of ur goals - /goals\n'
                'You can view the list of active goals, select any one and mark a new day of its achievement.\n\n'
                '🍿Switch language to russian - /russian\n\n'
                '🍿Return to english - /english')

new_rus = ('🌱Введите название новой цели!\n♨️Я хочу начать счет дней моей жизни без:')
new_eng = ('🌱Enter the name of the new goal!\n♨️I want to start counting the days of my life without:')


three_goals_rus = ('💢У вас слишком много целей!(3)')
three_goals_eng = ('💢You have too many goals!(3)')

choose_rus = ("📌Выбери любую из своих целей!")
choose_eng = ("📌Choose any of your goals!")

u_havent_rus = ('❗️У вас нет целей❗️\n🍃Для создания новой напишите /new')
u_havent_eng = ('❗️You have no goals❗️\n🍃To create a new one - /new')

new_day_rus = ('🟢Новый день отмечен!\n'
                'Напиши /goals для просмотра всех целей!🔶')
new_day_eng = ('🟢A new day has been checked!\n'
                'Write /goals to see all goals!🔶')

go_tomorrow_rus = ('🔴Сегодня ты уже отмечался.\n'
                'Возвращайся завтра!🔷')
go_tomorrow_eng = ('🔴You have already checked in today.\n'
                'Come back tomorrow!🔷')

sbiv_rus = ('❗️⭕️Твой счетчик дней сбит, ведь ты пропустил один или несколько.❗️⭕️\n'
                '♻️С сегодняшнего дня твоя цель начата сначала, так что количество дней будет равно 1!')
sbiv_eng = ('❗️⭕️Your day counter is hit because you missed one or more.❗️⭕️\n'
                '♻️From today on, your goal is started over again, so the number of days will be 1!')

deleted_rus = ('♻️Цель была успешно удалена!\nДля просмотра списка целей - /goals')
deleted_eng = ('♻️The goal was successfully deleted!\nTo view the list of goals - /goals')