from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import logging

AUTORIZATION = range(1)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

reply_keyboard = [
    ["Расписание на завтра", "Записать ДЗ"],
    ["Что на завтра задали",  "Расписание на неделю"]
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)


def start(update, context):
    user = update.message.chat.id
    print(user)
    if True:
        update.message.reply_text('Выберите действие, для продолжения работы', reply_markup=markup)

    # else:
    # update.message.reply_text("Пришлите токен для входа в аккаунт")
    # flag = True
    # while flag:
    #     text = update.message.text
    #     if text in "База данных":
    #         return AUTORIZATION
    #         else:
    #             update.message.reply_text("Ты позер, попробуй ещё раз!")


def authorization(update, context):
    update.message.reply_text("Регистрация пройдена успешно")
    update.message.reply_text('Выберите действие, для продолжения работы', reply_markup=markup)


def stop(update, context):
    update.message.reply_text("всё плохо")


def tomorrow(update, context):
    update.message.reply_text("Раздел расписания на завтра")


def homework(update, context):
    update.message.reply_text("Раздел записи ДЗ")


def tomorrow_homework(update, context):
    schedule = [[InlineKeyboardButton(f"Английский", callback_data='1'), InlineKeyboardButton(f"Русский", callback_data='2')],
                [InlineKeyboardButton(f"Физика", callback_data='3'), InlineKeyboardButton(f"Алгебра", callback_data='4')],
                [InlineKeyboardButton(f"Геометрия", callback_data='5'), InlineKeyboardButton(f"Физ-ра", callback_data='6')]]
    reply_keyboard = InlineKeyboardMarkup(schedule)

    update.message.reply_text("Раздел ДЗ на завтра", reply_markup=reply_keyboard)


def week(update, context):
    schedule = [
        [InlineKeyboardButton(f"Понедельник", callback_data='Monday'), InlineKeyboardButton(f"Вторник", callback_data='Tuesday')],
        [InlineKeyboardButton(f"Среда", callback_data='Wednesday'), InlineKeyboardButton(f"Четверг", callback_data='Thursday')],
        [InlineKeyboardButton(f"Пятница", callback_data='Friday'), InlineKeyboardButton(f"Суббота", callback_data='Saturday')]]
    reply_keyboard = InlineKeyboardMarkup(schedule)

    update.message.reply_text("Раздел расписания на неделю", reply_markup=reply_keyboard)


def main():
    updater = Updater('1757297275:AAFWjozUO911jvNakuoeoSS8m1yZaA5txTY', use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],

        states={
            # Добавили user_data для сохранения ответа.
            AUTORIZATION: [MessageHandler(Filters.text, authorization, pass_user_data=True)]},

        fallbacks=[MessageHandler(Filters.regex("^Stop&"), stop)]
    )
    # Команды бота
    dispatcher.add_handler(MessageHandler(Filters.regex('^Расписание на завтра$'), tomorrow))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Записать ДЗ$'), homework))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Что на завтра задали$'), tomorrow_homework))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Расписание на неделю$'), week))
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler("start", start))
    # # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
