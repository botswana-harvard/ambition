from .base import *

# overwrite LOGGING from .base to use syslog for logging
from .logging import LOGGING

# don't change!
DEBUG = False

ETC_DIR = os.path.join('/etc', APP_NAME)

SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'

# site is gaborone
SITE_ID = '10'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'ambition-test.bhp.org.bw',
    'ambition.clinicedc.org']

# static
STATIC_ROOT = os.path.join(str(Path(BASE_DIR).parent), 'static')


# see https://docs.djangoproject.com/en/2.0/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}


# ambition
# use the test rando list
# copy tests/'test_randomization_list.csv' to /etc/ambition
RANDOMIZATION_LIST_PATH = os.path.join(ETC_DIR, 'test_randomization_list.csv')


# django_crypto_fields
KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
# for first time use as a test UAT server
# AUTO_CREATE_KEYS = True
