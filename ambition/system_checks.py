import sys

from collections import namedtuple
from django.apps import apps as django_apps
from django.core.checks import Warning

err = namedtuple('Err', 'id cls')

error_configs = dict(
    randomization_list_check=err('ambition.W001', Warning),
)


def randomization_list_check(app_configs, **kwargs):
    check_failed = False
    errors = []
    error = error_configs.get('randomization_list_check')
    if 'test' not in sys.argv:
        model_cls = django_apps.get_model('ambition_rando.randomizationlist')
        if model_cls.objects.all().count() == 0:
            error_msg = 'Randomization list is not loaded. Run the management command.'
            check_failed = True
        if check_failed:
            errors.append(
                error.cls(
                    error_msg,
                    hint=None,
                    obj=None,
                    id=error.id,
                )
            )
    return errors
