from ..base import *
from ..logging import LOGGING

DEBUG = False

INDEX_PAGE = 'https://ambition.clinicedc.org'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'ambition.clinicedc.org']

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

# edc_sync / sync files
EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None

# edc_label
CUPS_SERVERS = {
    'bhp.printers.clinicedc.org': 'bhp.printers.clinicedc.org',
    'localhost': None}
