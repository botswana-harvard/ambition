from ambition_rando.admin_site import ambition_rando_admin
from ambition_subject.admin_site import ambition_subject_admin
from django.contrib import admin
from django.urls.conf import path, include
from django.views.generic.base import RedirectView
from edc_action_item.admin_site import edc_action_item_admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_base.views import LogoutView, LoginView
from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin
from edc_metadata.admin_site import edc_metadata_admin
from edc_pharmacy.admin_site import edc_pharmacy_admin
from edc_reference.admin_site import edc_reference_admin
from edc_registration.admin_site import edc_registration_admin
from edc_sync.admin import edc_sync_admin
from edc_sync_files.admin_site import edc_sync_files_admin

from .views import HomeView, AdministrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', edc_appointment_admin.urls),
    path('admin/', ambition_subject_admin.urls),
    path('admin/', edc_lab_admin.urls),
    path('admin/', edc_identifier_admin.urls),
    path('admin/', edc_metadata_admin.urls),
    path('admin/', edc_registration_admin.urls),
    path('admin/', edc_reference_admin.urls),
    path('admin/', edc_sync_admin.urls),
    path('admin/', ambition_rando_admin.urls),
    path('admin/', edc_pharmacy_admin.urls),
    path('admin/', edc_action_item_admin.urls),
    path('admin/edc_sync_files/', edc_sync_files_admin.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('admin/ambition_subject/', RedirectView.as_view(url='admin/ambition_subject/'),
         name='subject_models_url'),
    path('ambition_subject/', include('ambition_subject.urls')),
    path('subject/', include('ambition_dashboard.urls')),
    path('appointment/', include('edc_appointment.urls')),
    path('edc_action_item/', include('edc_action_item.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_consent/', include('edc_consent.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_lab/', include('edc_lab.urls')),
    path('edc_lab_dashboard/', include('edc_lab_dashboard.urls')),
    path('edc_pharmacy/', include('edc_pharmacy.urls')),
    path('edc_pharmacy_dashboard/', include('edc_pharmacy_dashboard.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('edc_metadata/', include('edc_metadata.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_identifier/', include('edc_identifier.urls')),
    path('edc_reference/', include('edc_reference.urls')),
    path('edc_registration/', include('edc_registration.urls')),
    path('edc_sync/', include('edc_sync.urls')),
    path('edc_sync_files/', include('edc_sync_files.urls')),
    path('edc_visit_schedule/', include('edc_visit_schedule.urls')),
    path('tz_detect/', include('tz_detect.urls')),
    path('login', LoginView.as_view(), name='login_url'),
    path('accounts/login/', LoginView.as_view(), name='login_url'),
    # path(r'^accounts/login/', include('registration.backends.hmac.urls')),
    path('logout', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]
