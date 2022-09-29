from .base import *

DEBUG = True

ALLOWED_HOSTS = ['ecommercerelucienteaseo.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'davsgd4n5s2bb6',
        'USER': 'gmoepcqkrcwzkr',
        'PASSWORD': 'a3866098a04bdbe74706d368f5e40e4266aeb3c5f46c209c6cfba3eb9f7bb180',
        'HOST': 'ec2-52-200-5-135.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}
STATICFILES_DIRS = (BASE_DIR, 'Ciclo_3Tienda/static/')