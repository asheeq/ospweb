from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoriesConfig(AppConfig):
    name = "ospweb.categories"
    verbose_name = _("Categories")

    def ready(self):
        try:
            from ospweb import categories  # noqa F401
        except ImportError:
            pass
