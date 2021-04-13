from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(update, context):
    user = update.message.chat.id
    if user in base:
        update.message.reply_text("Вы авторизированный пользователь")
    else:
        update.message.reply_text("Пришлите токен для входа в аккаунт")
        flag = True
        while flag:
            if update.message.text in base:
                update.message.reply_text("Все успешно!")
                flag = False
            else:
                update.message.reply_text("Ты позер, попробуй ещё раз!")



# def button(update, context):
#     query = update.callback_query
#     if query.data == 'pro':
#         file = open(f'./Users/{query.message.chat.id}.txt', 'w')
#         file.write(f'{query.data}')
#         file.close()
#         query.edit_message_text(text=f"Вы выбрали: {query.data} версию бота, теперь просто отправьте фото.")
#     if query.data == 'lite':
#         query.edit_message_text('Вы выбрали "LITE" версию бота,'
#                                 '\nчтобы начать отправлять фото, выберите один из предложенных языков:'
#                                 '\n/Russian - Русский'
#                                 '\n/English - Английский'
#                                 '\n/French - Французкий'
#                                 '\n/German - Немецкий')


# def language(update, context):
#     keyboard = [[InlineKeyboardButton("LITE", callback_data='lite')],
#                 [InlineKeyboardButton("PRO", callback_data='pro')]
#                 ]
#
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Выберите версию:', reply_markup=reply_markup)


# def language_lite(update, context):
#     file_r = open(f'./Users/{update.message.chat.id}.txt', 'r')
#     text = file_r.read()
#     file_r.close()
#     if text != 'pro':
#         update.message.reply_text('Вы находитесь в "LITE" версии бота,'
#                                     '\nчтобы изменить язык, выберите один из предложенных:'
#                                     '\n/Russian - Русский'
#                                     '\n/English - Английский'
#                                     '\n/French - Французкий'
#                                     '\n/German - Немецкий')
#     else:
#         update.message.reply_text('Смените режим бота на "LITE" версию, чтобы сменить язык.')

#
# def rus(update, context):
#     file = open(f'./Users/{update.message.chat.id}.txt', 'w')
#     file.write('rus')
#     file.close()
#     update.message.reply_text('Язык /Russian выбран, теперь отправьте фото текста на выбранном языке.')
#
#
# def eng(update, context):
#     file = open(f'./Users/{update.message.chat.id}.txt', 'w')
#     file.write('eng')
#     file.close()
#     update.message.reply_text('Язык /English выбран, теперь отправьте фото текста на выбранном языке.')
#
#
# def fra(update, context):
#     file = open(f'./Users/{update.message.chat.id}.txt', 'w')
#     file.write('fra')
#     file.close()
#     update.message.reply_text('Язык /French выбран, теперь отправьте фото текста на выбранном языке.')
#
#
# def frk(update, context):
#     file = open(f'./Users/{update.message.chat.id}.txt', 'w')
#     file.write('frk')
#     file.close()
#     update.message.reply_text('Язык /German выбран, теперь отправьте фото текста на выбранном языке.')
#

def info(update, context):
    update.message.reply_text('Бот создан для распознавания текcта с изображения, '
                              'он может работать в двух режимах: "PRO" и "LITE", '
                              'первый режим может максимально качественно распознать '
                              'текcт, изображенный на картинке с помощью нейросетей от GOOGLE, '
                              'но он будет платным. '
                              'Второй же режим позволит вам распознать текст с картинки бесплатно, '
                              'но не так качественно, как режим "PRO", так же для распознавания текста режимом "LITE" '
                              'нужно сфотографировать текст максимально хорошо, на однородном фоне и при этом'
                              'обрезав края. '
                              'Чтобы запустить бота выполните команду /start и следуйте инструкциям. Так же вы можете '
                              'воспользоваться командой /mods для изменения режима.')


def photo(update, context):
    # file_r = open(f'./Users/{update.message.chat.id}.txt', 'r')
    # text = file_r.read()
    # file_r.close()
    file = update.message.photo[-1]
    file_id = file.file_id
    NewFile = context.bot.get_file(file_id)
    NewFile.download(f'{file_id}.png')
    update.message.reply_text(text_dectect.main(f'{file_id}.png'))
    # else:
    #     update.message.reply_text(Photo.preob(update.message.chat.id, f'{file_id}.png'))
    # update.message.reply_text('Для распознавания текста с новой фотографии просто отправьте её:).'
    #                           '\nДля смены режима используйте /mods'
    #                           '\nДля смены языка в "LITE" режиме используйте /language_lite')
    # os.remove(f'./{file_id}.png')


def main():
    updater = Updater('1757297275:AAFWjozUO911jvNakuoeoSS8m1yZaA5txTY', use_context=True)

    dp = updater.dispatcher

    #
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    # dp.add_handler(CallbackQueryHandler(button))
    # dp.add_handler(CommandHandler("Russian", rus))
    # dp.add_handler(CommandHandler("English", eng))
    # dp.add_handler(CommandHandler("French", fra))
    # dp.add_handler(CommandHandler("German", frk))
    # dp.add_handler(CommandHandler("mods", language))
    # dp.add_handler(CommandHandler("language_lite", language_lite))

    dp.add_handler(MessageHandler(Filters.photo, photo))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
