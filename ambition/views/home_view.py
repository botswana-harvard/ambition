from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_navbar import NavbarViewMixin
from django.contrib import messages
from ambition_rando.randomizer import Randomizer


class HomeView(EdcBaseViewMixin, AppConfigViewMixin, NavbarViewMixin, TemplateView):

    app_config_name = 'ambition'
    template_name = 'ambition/home.html'

    navbar_name = 'ambition'
    navbar_selected_item = 'home'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.verify_sid_list()
        return context

    def verify_sid_list(self):
        model_cls = django_apps.get_model(Randomizer.sid_model)
        if model_cls.objects.all().count() == 0:
            messages.error(
                self.request,
                'Randomization list has not been loaded. '
                'Run the \'import_randomization_list\' management command '
                'to load before using the system.')
