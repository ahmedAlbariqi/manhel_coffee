from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    """
    هذه الفئة تسمح لنا بعرض نموذج الملف الشخصي بشكل مضمّن
    في صفحة تعديل المستخدم.
    """
    model = Profile
    can_delete = False
    verbose_name_plural = 'ملف شخصي'

class CustomUserAdmin(AuthUserAdmin):
    """
    هذه الفئة ترث من لوحة تحكم المستخدمين الافتراضية
    وتضيف إليها الـ Inline الخاص بالملف الشخصي.
    """
    inlines = (ProfileInline,)

# --- الخطوة الأهم ---
# بما أن جانغو يسجل نموذج User تلقائيًا، يجب علينا أولاً
# "إلغاء تسجيله" ثم "إعادة تسجيله" مع إعداداتنا المخصصة.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)