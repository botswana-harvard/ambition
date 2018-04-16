from .base_test import *

# site is gaborone
SITE_ID = 50

WSGI_APPLICATION = 'ambition.wsgi.capetown-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'capetown.uat.ambition.clinicedc.org']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}

TIME_ZONE = 'Africa/Johannesburg'
