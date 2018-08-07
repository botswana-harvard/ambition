from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('lilongwe')

WSGI_APPLICATION = 'ambition.wsgi.lilongwe.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'lilongwe.ambition.bhp.org.bw']

TIME_ZONE = 'Africa/Blantyre'
