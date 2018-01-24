
fqdn = 'ambition.clinicedc.org'

ambition_sites = (
    (1, 'reviewer'),
    (10, 'gaborone'),
    (20, 'harare'),
    (30, 'lilongwe'),
    (40, 'blantyre'),
    (50, 'capetown'),
    (60, 'kampala'),
)


def get_site_id(name):
    return [site for site in ambition_sites if site[1] == name][0][0]
