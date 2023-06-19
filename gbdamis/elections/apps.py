from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ElectionsConfig(AppConfig):
    name = "gbdamis.elections"
    verbose_name = _("Elections")

    def ready(self):
        try:
            import gbdamis.elections.signals  # noqa: F401
        except ImportError:
            pass
