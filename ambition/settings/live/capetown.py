from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('capetown')

WSGI_APPLICATION = 'ambition.wsgi.capetown.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'capetown.ambition.bhp.org.bw']

TIME_ZONE = 'Africa/Johannesburg'
