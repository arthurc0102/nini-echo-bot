from telegram import KeyboardButton, ReplyKeyboardMarkup

from .models import Job


def text_after_command(update):
    text = update.message.text
    entities = update.message.entities
    command_len = entities[0]['offset'] + entities[0]['length'] + 1
    return text[command_len:] if len(text) > command_len else ''


def set_status(user_id, chat_id, status):
    job, created = Job.objects.get_or_create(
        user_id=user_id,
        chat_id=chat_id,
        defaults={'status': status},
    )

    if created:
        return

    job.status = status
    job.save()


def build_reply_keyboard(nis,
                         resize_keyboard=True,
                         one_time_keyboard=True,
                         selective=True):

    keyboard = []
    keyboard_column = []

    for n in nis:
        if len(keyboard_column) == 2:
            keyboard.append(keyboard_column)
            keyboard_column = []
        keyboard_column.append(KeyboardButton(n.text))
    keyboard.append(keyboard_column)

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard,
        one_time_keyboard,
        selective,
    )
