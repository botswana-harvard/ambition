# Settings for development, e.g. tests, runserver

import sys

from .base import *

DEBUG = True

SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'

SITE_ID = 1

# use test rando list
RANDOMIZATION_LIST_PATH = os.path.join(
    BASE_DIR, APP_NAME, 'tests', 'test_randomization_list.csv')

CUPS_SERVERS = {
    'bhp.printers.clinicedc.org': 'bhp.printers.clinicedc.org',
    'localhost': None}

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
