from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthenticationConfig(AppConfig):
    name = "gbdamis.authentication"
    verbose_name = _("Authentication")

    def ready(self):
        try:
            import gbdamis.authentication.signals  # noqa: F401
        except ImportError:
            pass
