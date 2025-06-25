from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        """
        عندما يكون التطبيق جاهزًا، قم باستيراد ملف النماذج (الذي يحتوي على الإشارات).
        """
        # --- هذا هو السطر الوحيد الذي تم تغييره ---
        import apps.users.models