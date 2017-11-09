from edc_navbar import NavbarItem, site_navbars, Navbar

ambition = Navbar(name='ambition')

ambition.append_item(
    NavbarItem(
        name='screened_subject',
        title='Screening',
        label='Screening',
        url_name='ambition_dashboard:screening_listboard_url'))

ambition.append_item(
    NavbarItem(
        name='consented_subject',
        title='Subjects',
        label='Subjects',
        url_name='ambition_dashboard:listboard_url'))

ambition.append_item(
    NavbarItem(
        name='pharmacy',
        title='Pharmacy',
        fa_icon='fa-medkit',
        url_name=f'edc_pharmacy_dashboard:home_url'))

ambition.append_item(
    NavbarItem(
        name='lab',
        title='Specimens',
        fa_icon='fa-flask',
        url_name='edc_lab_dashboard:home_url'))

site_navbars.register(ambition)
