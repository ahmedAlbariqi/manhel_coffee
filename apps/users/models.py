from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    """
    نموذج لتوسيع معلومات المستخدم الأساسي.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("المستخدم"))
    address = models.TextField(_("العنوان"), blank=True, null=True)
    phone_number = models.CharField(_("رقم الهاتف"), max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(_("الصورة الشخصية"), upload_to='profiles/', blank=True, null=True)

    class Meta:
        verbose_name = _("ملف شخصي")
        verbose_name_plural = _("ملفات شخصية")

    def __str__(self):
        return f"ملف شخصي للمستخدم: {self.user.username}"


# ===================================================================
# الإشارات (Signals) - لإنشاء الملف الشخصي تلقائيًا مع كل مستخدم جديد
# ===================================================================

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    إشارة يتم إطلاقها بعد حفظ مستخدم جديد.
    إذا كان المستخدم جديدًا (created=True)، قم بإنشاء ملف شخصي له.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    إشارة يتم إطلاقها بعد حفظ المستخدم، وتقوم بحفظ الملف الشخصي المرتبط به.
    """
    instance.profile.save()