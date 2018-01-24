# lilongwe.ambition gunicorn.conf
import os

SOURCE_ROOT = os.path.expanduser('~/')
errorlog = os.path.join(SOURCE_ROOT, 'logs/ambition-gunicorn-error.log')
accesslog = os.path.join(SOURCE_ROOT, 'logs/ambition-gunicorn-access.log')
loglevel = 'debug'
workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

bind = "127.0.0.1:9102"
