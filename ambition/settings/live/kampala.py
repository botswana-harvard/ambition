from ...sites import get_site_id
from ..test.base_test import *

# for django.contrib.sites
SITE_ID = get_site_id('kampala')

WSGI_APPLICATION = 'ambition.wsgi.kampala.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'kampala.ambition.clinicedc.org']

TIME_ZONE = 'Africa/Kampala'
