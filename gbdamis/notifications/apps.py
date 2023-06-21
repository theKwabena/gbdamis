from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gbdamis.notifications"
    verbose_name = _("Notifications")

    def ready(self):
        try:
            import gbdamis.authentication.signals  # noqa: F401
        except ImportError:
            pass
