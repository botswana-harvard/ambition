# capetown.ambition gunicorn.conf
import os

errorlog = '/var/log/ambition-gunicorn-error.log'
accesslog = '/var/log/ambition-gunicorn-access.log'
loglevel = 'debug'
workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

bind = "127.0.0.1:9050"
