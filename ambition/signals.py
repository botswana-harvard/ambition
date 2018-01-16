from ambition.sites import ambition_sites, fqdn
from django.apps import apps as django_apps
from django.db.models.signals import post_migrate
from django.dispatch.dispatcher import receiver
from edc_base.sites.add_or_update_django_sites import add_or_update_django_sites


def post_migrate_update_sites(sender=None, **kwargs):
    add_or_update_django_sites(
        apps=django_apps, sites=ambition_sites, fqdn=fqdn)
