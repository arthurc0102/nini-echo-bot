import logging

from telegram import ReplyKeyboardRemove

from . import helpers, repositories
from .models import Ni, Job


# Set logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def ni(bot, update):
    chat_id = update.message.chat.id
    reply = helpers.text_after_command(update)

    if not reply:
        _ni = repositories.random_ni(chat_id)
        reply = _ni.text if _ni else '沒東西還想要我怎樣逆'

    bot.send_message(chat_id, '{}逆'.format(reply))


def ni_list(bot, update):
    nis = repositories.chat_nis(update.message.chat.id)
    ni_data = ['{}. {}逆'.format(i, _ni.text) for i, _ni in enumerate(nis, 1)]
    update.message.reply_text('\n'.join(ni_data) or '空空如也', quote=False)


def add(bot, update):
    helpers.set_status(
        update.message.from_user.id,
        update.message.chat.id,
        Job.ADD
    )
    update.message.reply_text('你要新增什麼呢？')


def edit(bot, update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    nis = repositories.user_nis(user_id, chat_id)
    if not nis:
        update.message.reply_text('你沒有建立任何逆喔！')
        return

    reply_markup = helpers.build_reply_keyboard(nis)
    helpers.set_status(user_id, chat_id, Job.EDIT)
    update.message.reply_text('請選擇要編輯的項目', reply_markup=reply_markup)


def delete(bot, update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    nis = repositories.user_nis(user_id, chat_id)
    if not nis:
        update.message.reply_text('你沒有建立任何逆喔！')
        return

    reply_markup = helpers.build_reply_keyboard(nis)
    helpers.set_status(user_id, chat_id, Job.DELETE)
    update.message.reply_text('請選擇要刪除的項目', reply_markup=reply_markup)


def cancel(bot, update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    repositories.user_job(user_id, chat_id).delete()
    update.message.reply_text('已取消～', reply_markup=ReplyKeyboardRemove())


def ni_add(update, job):
    Ni.objects.create(
        user_id=update.message.from_user.id,
        chat_id=update.message.chat.id,
        text=update.message.text
    )

    return True


def ni_edit(update, job):
    _ni = repositories.target_ni(
        update.message.from_user.id,
        update.message.chat.id,
        update.message.text,
    )

    if job.target:
        job.target.text = update.message.text
        job.target.save()
        return True

    if not _ni:
        return

    job.target = _ni
    job.save()
    update.message.reply_text(
        '請輸入你的新內容',
        reply_markup=ReplyKeyboardRemove()
    )

    return False


def ni_delete(update, job):
    _ni = repositories.target_ni(
        update.message.from_user.id,
        update.message.chat.id,
        update.message.text,
    )

    if not _ni:
        return

    _ni.delete()
    return True


def text_message(bot, update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id

    job = repositories.user_job(user_id, chat_id).first()
    if not job:
        return

    finished = {
        Job.ADD: ni_add,
        Job.EDIT: ni_edit,
        Job.DELETE: ni_delete,
    }[job.status](update, job)

    if finished is None:
        update.message.reply_text('你沒有權限更動這個逆喔！')
        return

    if not finished:
        return

    job.delete()
    update.message.reply_text(
        '已經完成你的要求啦～',
        reply_markup=ReplyKeyboardRemove()
    )
