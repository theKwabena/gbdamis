from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DuesConfig(AppConfig):
    name = "gbdamis.dues"
    verbose_name = _("Dues")

    def ready(self):
        try:
            import gbdamis.dues.signals  # noqa: F401
        except ImportError:
            pass
