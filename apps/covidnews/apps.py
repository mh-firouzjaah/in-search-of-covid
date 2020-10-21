from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CovidNewsAppConfig(AppConfig):
    name = 'apps.covidnews'

    verbose_name = _('CovidNews')
    verbose_name_plural = _('CovidNews')
