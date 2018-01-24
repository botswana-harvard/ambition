# gaborone.ambition gunicorn.conf
import os

SOURCE_ROOT = os.path.expanduser('~/source/ambition')

errorlog = os.path.join(SOURCE_ROOT, 'log/ambition-gunicorn-error.log')
accesslog = os.path.join(SOURCE_ROOT, 'log/ambition-gunicorn-access.log')
loglevel = 'debug'
pidfile = os.path.join(SOURCE_ROOT, 'run/ambition-gaborone.pid')

workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

raw_env = [f'DJANGO_SETTINGS_MODULE=ambition.settings.production.gaborone']

bind = "127.0.0.1:9010"
