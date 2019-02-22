from .models import Ni, Job


def random_ni(chat_id):
    return Ni.objects\
        .filter(chat_id=chat_id)\
        .order_by('?')\
        .first()


def chat_nis(chat_id):
    return Ni.objects.filter(chat_id=chat_id)


def user_nis(user_id, chat_id):
    return Ni.objects.filter(user_id=user_id, chat_id=chat_id)


def target_ni(user_id, chat_id, text):
    return Ni.objects\
        .filter(user_id=user_id, chat_id=chat_id, text=text)\
        .first()


def user_job(user_id, chat_id):
    return Job.objects.filter(user_id=user_id, chat_id=chat_id)
