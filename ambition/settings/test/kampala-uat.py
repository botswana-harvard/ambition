from .base_test import *

# site is kampala
SITE_ID = 60

WSGI_APPLICATION = 'ambition.wsgi.kampala-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'kampala.uat.ambition.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}

TIME_ZONE = 'Africa/Gaborone'
