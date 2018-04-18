
fqdn = 'ambition.bhp.org.bw'

ambition_sites = (
    (1, 'reviewer', ''),
    (10, 'gaborone', 'Botswana-Harvard Partnership'),
    (20, 'harare', 'University of Zimbabwe'),
    (30, 'lilongwe', 'UNC Project Malawi'),
    (40, 'blantyre', 'Malawi Liverpool Wellcome Trust Clinical Research Programme'),
    (50, 'capetown', 'University of Cape Town'),
    (60, 'kampala', 'IDI Uganda'),
)


def get_site_id(name):
    try:
        return [site for site in ambition_sites if site[1] == name][0][0]
    except IndexError:
        return [site for site in ambition_sites if site[2] == name][0][0]
