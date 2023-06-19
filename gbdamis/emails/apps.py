# from django.apps import AppConfig


# class EmailsConfig(AppConfig):
#     default_auto_field = "django.db.models.BigAutoField"
#     name = "emails"
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmailsConfig(AppConfig):
    name = "gbdamis.emails"
    verbose_name = _("Emails")

    def ready(self):
        try:
            import gbdamis.emails.signals  # noqa: F401
        except ImportError:
            pass
