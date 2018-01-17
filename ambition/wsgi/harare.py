import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("ambition.settings.production.harare")

application = get_wsgi_application()
