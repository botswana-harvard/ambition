from .base_test import *

# site is gaborone
SITE_ID = 40

WSGI_APPLICATION = 'ambition.wsgi.blantyre-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'blantyre.uat.ambition.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}

TIME_ZONE = 'Africa/Blantyre'
