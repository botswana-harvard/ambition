from edc_base import NavbarItem
from edc_lab_dashboard.navbars import navbar_items as edc_lab_navbar_items
from edc_pharma_dashboard.navbars import navbar_items as edc_pharma_navbar_items

navbars = {}
navbar_items = []
config = [
    ('consented_subject', 'ambition_dashboard', 'Subjects',
     'fa-user-circle-o', 'listboard_url_name'),
    ('screened_subject', 'ambition_dashboard', 'Screening',
     'fa-user-circle-o', 'screening_listboard_url_name'),
    ('lab', 'edc_lab_dashboard', None, 'fa-flask', 'home_url_name'),
    ('pharma', 'edc_pharma_dashboard', None, 'fa-medkit', 'home_url_name')
]
for name, app_config_name, label, fa_icon, app_config_attr in config:
    navbar_item = NavbarItem(
        name=name,
        app_config_name=app_config_name,
        label=label,
        fa_icon=fa_icon,
        app_config_attr=app_config_attr)
    navbar_items.append(navbar_item)
navbars.update(default=navbar_items)

navbars.update(specimens=edc_lab_navbar_items)
navbars.update(pharma=edc_pharma_navbar_items)
