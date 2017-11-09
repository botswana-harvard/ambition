
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_navbar import NavbarViewMixin
from edc_base.view_mixins import AdministrationViewMixin


class AdministrationView(EdcBaseViewMixin, AppConfigViewMixin,
                         NavbarViewMixin, AdministrationViewMixin, TemplateView):

    # template_name = 'ambition/administration.html'
    app_config_name = 'ambition'

    navbar_name = 'ambition'
    navbar_selected_item = 'administration'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
