from .base import *

DEBUG = True

ALLOWED_HOSTS = ['ecommercerelucienteaseo.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dac7fdnuj6uftu',
        'USER': 'knxyomphnrslwo',
        'PASSWORD': '7a4a7006b4bd51336cb04361cafaebe9a3654d5ae7a71c2e43ea9ea3cb6879ce',
        'HOST': 'ec2-34-200-205-45.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}
STATICFILES_DIRS = (BASE_DIR, 'static')