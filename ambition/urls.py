from ambition_ae.admin_site import ambition_ae_admin
from ambition_prn.admin_site import ambition_prn_admin
from ambition_screening.admin_site import ambition_screening_admin
from ambition_subject.admin_site import ambition_subject_admin
from django.contrib import admin
from django.urls.conf import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView
from edc_action_item.admin_site import edc_action_item_admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin
from edc_locator.admin_site import edc_locator_admin
from edc_metadata.admin_site import edc_metadata_admin
from edc_pharmacy.admin_site import edc_pharmacy_admin
from edc_reference.admin_site import edc_reference_admin
from edc_registration.admin_site import edc_registration_admin
from edc_sync.admin import edc_sync_admin
from edc_sync_files.admin_site import edc_sync_files_admin
from edc_visit_schedule.admin_site import edc_visit_schedule_admin

from .views import HomeView, AdministrationView
from django.conf import settings

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),
    #     path('accounts/login/', LoginView.as_view(), name='login'),
    #     path('admin/login/', LoginView.as_view(), name='login'),
    #     path('accounts/logout/', LogoutView.as_view(
    #         template_name='edc_base/login.html'), name='logout'),
    #     path('admin/logout/', LogoutView.as_view(
    #         template_name='edc_base/login.html'), name='logout'),
    #     path('accounts/password_reset/', LogoutView.as_view(
    #         template_name='edc_base/login.html'), name='password_reset'),
    #     path('accounts/password_reset/done/', LogoutView.as_view(
    #         template_name='edc_base/login.html'), name='password_reset_done'),
    #     path('accounts/reset/<uidb64>/<token>/', LogoutView.as_view(
    #         template_name='edc_base/login.html'), name='password_reset_confirm'),
    #     path('accounts/reset/done/', LogoutView.as_view(
    # template_name='edc_base/login.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('admin/', edc_appointment_admin.urls),
    path('admin/', ambition_subject_admin.urls),
    path('admin/', ambition_ae_admin.urls),
    path('admin/', ambition_prn_admin.urls),
    path('admin/', ambition_screening_admin.urls),
    path('admin/', edc_lab_admin.urls),
    path('admin/', edc_locator_admin.urls),
    path('admin/', edc_identifier_admin.urls),
    path('admin/', edc_metadata_admin.urls),
    path('admin/', edc_registration_admin.urls),
    path('admin/', edc_reference_admin.urls),
    path('admin/', edc_sync_admin.urls),
    path('admin/', edc_pharmacy_admin.urls),
    path('admin/', edc_action_item_admin.urls),
    path('admin/edc_visit_schedule/', edc_visit_schedule_admin.urls),
    path('admin/edc_sync_files/', edc_sync_files_admin.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('admin/ambition_subject/', RedirectView.as_view(url='admin/ambition_subject/'),
         name='subject_models_url'),
    path('ambition_subject/', include('ambition_subject.urls')),
    path('ambition_ae/', include('ambition_ae.urls')),
    path('ambition_prn/', include('ambition_prn.urls')),
    path('ambition_screening/', include('ambition_screening.urls')),
    path('subject/', include('ambition_dashboard.urls')),
    path('appointment/', include('edc_appointment.urls')),
    path('edc_action_item/', include('edc_action_item.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_consent/', include('edc_consent.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_lab/', include('edc_lab.urls')),
    path('edc_lab_dashboard/', include('edc_lab_dashboard.urls')),
    path('edc_locator/', include('edc_locator.urls')),
    path('edc_pharmacy/', include('edc_pharmacy.urls')),
    # path('edc_pharmacy_dashboard/', include('edc_pharmacy_dashboard.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('edc_metadata/', include('edc_metadata.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_identifier/', include('edc_identifier.urls')),
    path('edc_reference/', include('edc_reference.urls')),
    path('edc_registration/', include('edc_registration.urls')),
    path('edc_subject_dashboard/', include('edc_subject_dashboard.urls')),
    path('edc_sync/', include('edc_sync.urls')),
    path('edc_sync_files/', include('edc_sync_files.urls')),
    path('edc_visit_schedule/', include('edc_visit_schedule.urls')),
    path('tz_detect/', include('tz_detect.urls')),
    path('switch_sites/', LogoutView.as_view(next_page=settings.INDEX_PAGE),
         name='switch_sites_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]
