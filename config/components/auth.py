# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

password_validation = 'django.contrib.auth.password_validation.'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': password_validation + 'UserAttributeSimilarityValidator',
    },
    {
        'NAME': password_validation + 'MinimumLengthValidator',
    },
    {
        'NAME': password_validation + 'CommonPasswordValidator',
    },
    {
        'NAME': password_validation + 'NumericPasswordValidator',
    },
]
