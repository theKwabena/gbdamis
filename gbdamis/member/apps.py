from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MembersConfig(AppConfig):
    name = "gbdamis.members"
    verbose_name = _("Members")

    def ready(self):
        try:
            import gbdamis.members.signals  # noqa: F401
        except ImportError:
            pass
