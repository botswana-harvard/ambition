from edc_base.sites.add_or_update_django_sites import add_or_update_django_sites

fqdn = 'ambition.bhp.org.bw'

ambition_sites = (
    ('10', 'gaborone'),
    ('20', 'harare'),
    ('30', 'lilongwe'),
    ('40', 'blantyre'),
    ('50', 'capetown'),
    ('60', 'kampala'),
)


def add_or_update_ambition_sites(apps, schema_editor):
    add_or_update_django_sites(apps, ambition_sites, fqdn)
