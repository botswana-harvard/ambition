from .base_test import *

# site is gaborone
SITE_ID = 10

WSGI_APPLICATION = 'ambition.wsgi.train.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'train.ambition.clinicedc.org']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'train.conf'),
        },
    },
}
