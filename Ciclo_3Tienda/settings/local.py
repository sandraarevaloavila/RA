from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'relucienteaseo',
        'USER': 'usuarioadministrador',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
STATICFILES_DIRS = [

    BASE_DIR / r"C:\Users\Nidia\PycharmProjects\Ciclo_3Tienda\static",
]