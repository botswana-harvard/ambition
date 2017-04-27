import arrow

from dateutil.tz import gettz
from datetime import datetime

from django.apps import apps as django_apps

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

app_config = django_apps.get_app_config('edc_protocol')

tzinfo = gettz('Africa/Gaborone')

v1 = Consent(
    'ambition_subject.subjectconsent',
    version='1',
    start=arrow.get(
        datetime(2016, 12, 31, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2018, 12, 31, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=18,
    age_is_adult=18,
    age_max=64,
    gender=[MALE, FEMALE])
site_consents.register(v1)
