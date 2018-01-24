import os

from .base import *

ETC_DIR = os.path.join('/etc', APP_NAME, 'live')

RANDOMIZATION_LIST_PATH = os.path.join(ETC_DIR, 'randomization_list.csv')

# django_crypto_field
KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
AUTO_CREATE_KEYS = False

with open(os.path.join(ETC_DIR, 'secret_key')) as f:
    SECRET_KEY = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(ETC_DIR, 'mysql.conf'),
        },
    },
}
