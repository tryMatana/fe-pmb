# ===== apps.py =====
from django.apps import AppConfig


class PmbPublicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pmb_public'