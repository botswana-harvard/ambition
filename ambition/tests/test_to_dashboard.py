import sys

from ambition_rando.import_randomization_list import import_randomization_list
from django.apps import apps as django_apps
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.management.color import color_style
from django.test.utils import override_settings, tag
from django.urls.base import reverse
from edc_appointment.constants import IN_PROGRESS_APPT, SCHEDULED_APPT
from edc_appointment.models.appointment import Appointment
from model_mommy import mommy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver
from django.conf import settings
from edc_lab_dashboard.dashboard_urls import dashboard_urls
from django.urls.exceptions import NoReverseMatch

style = color_style()

SYSTEM_COLUMNS = [
    'created', 'modified', 'user_created', 'user_modified',
    'hostname_created', 'hostname_modified',
    'device_created', 'device_modified', 'revision', 'id',
    'subject_identifier_as_pk', 'subject_identifier_aka',
    'slug', ]


class SeleniumLoginMixin:

    def setUp(self):
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com')
        super().setUp()

    def login(self):
        """Edc login with custom template.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('admin')
        self.selenium.find_element_by_xpath('//input[@value="Submit"]').click()
        self.selenium.implicitly_wait(3)


class SeleniumTestModelFormMixin:

    def fill_form(self, model=None, obj=None, exclude=None,
                  values=None, save=None,
                  save_value=None, verbose=None):
        """Fills a django modelform taking values from a given object.

        If not obj, tries to get the mommy receipe for the model.

        For example:
            self.fill_form(
                model=self.subject_screening_model,
                obj=obj, exclude=['subject_identifier', 'report_datetime'])
        """
        save = True if save is None else save
        save_value = save_value or 'Save'
        values = values or {}
        if not obj:
            sys.stdout.write(style.WARNING(
                f'Using mommy recipe. model={model}\n'))
            obj = mommy.prepare_recipe(model, **values)
        # assert on django modelform
        form_id = f'{model.split(".")[1]}_form'
        self.selenium.find_element_by_xpath(f"//form[@id='{form_id}']")
        # loop on fields
        fields = self.fields(model=model, exclude=exclude)
        for field in fields:
            element = None
            value = values.get(field.name) or getattr(obj, field.name)
            if verbose:
                sys.stdout.write(f'{field.name}={value}\n')
            if value:
                try:
                    if not field.name.endswith('_datetime'):
                        element = self.selenium.find_element_by_xpath(
                            f"//input[@name='{field.name}']")
                except NoSuchElementException as e:
                    sys.stdout.write(style.ERROR(f'{e}\n'))
                else:
                    if element and verbose:
                        sys.stdout.write(
                            f'{field.name}, {element.tag_name}, '
                            f'{element.get_attribute("class")})\n')
                    if field.name.endswith('_datetime'):  # edc naming convention
                        element = self.selenium.find_element_by_xpath(
                            f"//input[@id='id_{field.name}_0']")
                        element.clear()
                        element.send_keys(value.strftime('%Y-%m-%d'))
                        element = self.selenium.find_element_by_xpath(
                            f"//input[@id='id_{field.name}_1']")
                        element.clear()
                        element.send_keys(value.strftime('%H:%M'))
                    elif element.get_attribute('class') == 'vDateField':
                        element.send_keys(value.strftime('%Y-%m-%d'))
                    elif element.get_attribute('class') == 'radiolist':
                        for index in range(0, len(field.choices)):
                            try:
                                element = self.selenium.find_element_by_xpath(
                                    f"//input[@id='id_{field.name}_{index}']")
                            except NoSuchElementException as e:
                                sys.stdout.write(style.ERROR(f'{e}\n'))
                                break
                            else:
                                if element.get_attribute('value') == value:
                                    element.click()
                                    break
                    else:
                        element.send_keys(value)
        if save:
            element = self.selenium.find_element_by_xpath(
                f"//input[@value='{save_value}']")
            element.click()
        model_cls = django_apps.get_model(model)
        return model_cls.objects.all().order_by('modified').last()

    def fields(self, model=None, exclude=None):
        """Returns all field classes that might be on the form.

        Use exclude to avoid unnecessarily attempting to find an element
        known not to eb on the form for this case.
        """
        model_cls = django_apps.get_model(model)
        fields = [
            f for f in model_cls._meta.fields
            if f.name not in SYSTEM_COLUMNS and f.editable and f.name not in exclude]
        return fields


@override_settings(DEBUG=True)
class MySeleniumTests(SeleniumLoginMixin, SeleniumTestModelFormMixin, StaticLiveServerTestCase):

    appointment_model = 'edc_appointment.appointment'
    subject_screening_model = 'ambition_subject.subjectscreening'
    subject_consent_model = 'ambition_subject.subjectconsent'
    extra_url_names = [
        'home_url',
        'administration_url']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        import_randomization_list()
        url_names = (self.extra_url_names
                     + list(settings.DASHBOARD_URL_NAMES.values())
                     + list(settings.LAB_DASHBOARD_URL_NAMES.values())
                     + list(dashboard_urls.values()))
        self.url_names = list(set(url_names))
        super().setUp()

    @tag('1')
    def test_navbar_urls(self):
        """Follows any url that can be reversed without kwargs.
        """
        self.login()
        for url_name in self.url_names:
            try:
                url = reverse(url_name)
            except NoReverseMatch:
                sys.stdout.write(style.ERROR(f'NoReverseMatch: {url_name}\n'))
            else:
                sys.stdout.write(style.SUCCESS(f'{url_name} {url}\n'))
                self.selenium.get('%s%s' % (self.live_server_url, url))
                self.selenium.implicitly_wait(2)

    def test_subject_screening_to_subject_dashboard(self):
        self.login()

        url = reverse(settings.DASHBOARD_URL_NAMES.get(
            'screening_listboard_url'))
        self.selenium.get('%s%s' % (self.live_server_url, url))
        self.selenium.implicitly_wait(3)
        self.selenium.find_element_by_id('subjectscreening_add').click()
        self.selenium.implicitly_wait(10)

        # add a subject screening form
        obj = mommy.prepare_recipe(self.subject_screening_model)
        model_obj = self.fill_form(
            model=self.subject_screening_model,
            obj=obj, exclude=['subject_identifier', 'report_datetime'])

        # assert back at screening listboard
        self.selenium.find_element_by_id('subjectscreening_add')

        # change a subject screening form
        self.selenium.find_element_by_id(
            f'subjectscreening_change_{model_obj.screening_identifier}').click()
        self.selenium.find_element_by_xpath(f"//input[@value='Save']").click()

        # add a subject consent for the newly screening subject
        self.selenium.find_element_by_id(
            f'subjectconsent_add_{model_obj.screening_identifier}').click()

        obj = mommy.prepare_recipe(
            self.subject_consent_model,
            **{'screening_identifier': model_obj.screening_identifier,
               'dob': model_obj.estimated_dob,
               'gender': model_obj.gender})
        obj.initials = f'{obj.first_name[0]}{obj.last_name[0]}'
        model_obj = self.fill_form(
            model=self.subject_consent_model, obj=obj,
            exclude=['subject_identifier', 'citizen', 'legal_marriage',
                     'marriage_certificate', 'subject_type',
                     'gender', 'study_site'],
            verbose=True)

        # assert reached at subject dashboard
        self.selenium.find_element_by_id(f'subject_dashboard')

        # set appointment in progress
        subject_identifier = model_obj.subject_identifier
        appointment = Appointment.objects.filter(
            subject_identifier=subject_identifier).order_by('timepoint')[0]
        self.selenium.find_element_by_id(
            f'start_btn_{appointment.visit_code}_'
            f'{appointment.visit_code_sequence}').click()
        model_obj = self.fill_form(
            model=self.appointment_model, obj=appointment,
            values={'appt_status': IN_PROGRESS_APPT,
                    'appt_reason': SCHEDULED_APPT},
            exclude=['subject_identifier',
                     'timepoint_datetime', 'timepoint_status',
                     'facility_name'],
            verbose=True)

        self.selenium.implicitly_wait(10)
        # assert back at subject_dashboard
        self.selenium.find_element_by_id(f'subject_dashboard')

        # change a subject consent form
