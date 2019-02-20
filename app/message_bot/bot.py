from config.components.bot import TG_TOKEN

from telegram import Bot as TelegramBot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

from . import callbacks


def webhook_handler(data):
    bot = TelegramBot(TG_TOKEN)
    dispatcher = Dispatcher(bot, None)

    # Handlers
    dispatcher.add_handler(CommandHandler('ni', callbacks.ni))
    dispatcher.add_handler(CommandHandler('list', callbacks.ni_list))
    dispatcher.add_handler(CommandHandler('add', callbacks.add))
    dispatcher.add_handler(CommandHandler('edit', callbacks.edit))
    dispatcher.add_handler(CommandHandler('delete', callbacks.delete))
    dispatcher.add_handler(CommandHandler('cancel', callbacks.cancel))
    dispatcher.add_handler(MessageHandler(Filters.text, callbacks.text_message))  # NOQA

    # Process update
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)
