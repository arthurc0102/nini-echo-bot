from config.settings import env


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'
