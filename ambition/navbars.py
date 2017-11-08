from edc_navbar import NavbarItem, site_navbars, Navbar

ambition = Navbar(name='ambition')

ambition.append_item(
    NavbarItem(
        name='screened_subject',
        title='Screening',
        label='screening',
        fa_icon='fa-user-circle-o',
        url_name='ambition_dashboard:screening_listboard_url'))

ambition.append_item(
    NavbarItem(
        name='consented_subject',
        title='Subjects',
        label='subjects',
        fa_icon='fa-user-circle-o',
        url_name='ambition_dashboard:listboard_url'))

ambition.append_item(
    NavbarItem(
        name='lab',
        label='edc_lab',
        fa_icon='fa-flask',
        url_name='edc_lab_dashboard:home_url'))

site_navbars.register(ambition)
