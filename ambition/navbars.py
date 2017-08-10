from edc_base import NavbarItem
from edc_lab_dashboard.navbars import navbar_items as edc_lab_navbar_items

navbars = {}
navbar_items = []
config = [
    ('ambition_dashboard', 'Subjects', 'fa-user-circle-o', 'listboard_url_name'),
    ('ambition_dashboard', 'Screening',
     'fa-user-circle-o', 'listboard_url_name'),
    ('edc_lab_dashboard', None, 'fa-flask', 'home_url_name')
]
for app_config_name, label, fa_icon, app_config_attr in config:
    navbar_item = NavbarItem(
        app_config_name=app_config_name,
        label=label,
        fa_icon=fa_icon,
        app_config_attr=app_config_attr)
    navbar_items.append(navbar_item)
navbars.update(default=navbar_items)

navbars.update(specimens=edc_lab_navbar_items)
