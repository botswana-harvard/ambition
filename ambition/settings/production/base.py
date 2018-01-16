from ..base import *
from ..logging import LOGGING

DEBUG = False

ETC_DIR = os.path.join('/etc', APP_NAME)

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'ambition.clinicedc.org']

with open(os.path.join(ETC_DIR, 'secret_key')) as f:
    SECRET_KEY = f.read().strip()

# see https://docs.djangoproject.com/en/2.0/topics/cache/
# requires memcache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}

# static
STATIC_ROOT = os.path.join(str(Path(BASE_DIR).parent), 'static')

# edc app specific settings  ################

# django_crypto_field
KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
AUTO_CREATE_KEYS = False

# edc_sync / sync files
EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None

# ambition
# copy final randomization_list.csv' to /etc/ambition
RANDOMIZATION_LIST_PATH = os.path.join(ETC_DIR, 'randomization_list.csv')
