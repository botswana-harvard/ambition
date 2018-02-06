from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('reviewer')

WSGI_APPLICATION = 'ambition.wsgi.reviewer.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'reviewer.ambition.clinicedc.org']

TIME_ZONE = 'Africa/Gaborone'
