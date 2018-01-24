import os

SOURCE_ROOT = os.path.expanduser('~/')
errorlog = os.path.join(SOURCE_ROOT, 'log/ambition-test-gunicorn-error.log')
accesslog = os.path.join(SOURCE_ROOT, 'log/ambition-test-gunicorn-access.log')
loglevel = 'debug'
workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

pidfile = os.path.join(SOURCE_ROOT, 'run/ambition-train.pid')

raw_env = [f'DJANGO_SETTINGS_MODULE=ambition.settings.production.train']

bind = "127.0.0.1:9102"
