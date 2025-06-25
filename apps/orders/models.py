from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.products.models import Product

class Order(models.Model):
    """
    يمثل الطلب الواحد للعميل.
    """
    class OrderStatus(models.TextChoices):
        NEW = 'NE', _('طلب جديد')
        PROCESSING = 'PR', _('قيد التجهيز')
        SHIPPED = 'SH', _('تم الشحن')
        DELIVERED = 'DE', _('تم التوصيل')
        CANCELED = 'CA', _('ملغي')

    # --- علاقات ---
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # نحتفظ بالطلب حتى لو حذف المستخدم حسابه
        null=True,
        blank=True,
        related_name='orders',
        verbose_name=_("المستخدم")
    )
    
    # --- معلومات العميل (نسخة لحظة الشراء) ---
    first_name = models.CharField(_("الاسم الأول"), max_length=50)
    last_name = models.CharField(_("الاسم الأخير"), max_length=50)
    email = models.EmailField(_("البريد الإلكتروني"))
    phone = models.CharField(_("رقم الهاتف"), max_length=20)
    address = models.CharField(_("العنوان"), max_length=250)
    city = models.CharField(_("المدينة"), max_length=100)

    # --- معلومات الطلب ---
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التحديث"), auto_now=True)
    paid = models.BooleanField(_("مدفوع"), default=False)
    status = models.CharField(
        _("حالة الطلب"), max_length=2, choices=OrderStatus.choices, default=OrderStatus.NEW
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")

    def __str__(self):
        return f"طلب رقم {self.id}"

    def get_total_cost(self):
        """
        يحسب التكلفة الإجمالية للطلب.
        """
        return sum(item.get_cost() for item in self.items.all())
    get_total_cost.short_description = 'الإجمالي'


class OrderItem(models.Model):
    """
    يمثل المنتج الواحد داخل الطلب.
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name=_("الطلب"))
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.SET_NULL, # نحتفظ بالبند حتى لو حذف المنتج من المتجر
        null=True,
        verbose_name=_("المنتج")
    )
    # --- نسخة من السعر والكمية لحظة الشراء ---
    price = models.DecimalField(_("السعر"), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_("الكمية"), default=1)

    class Meta:
        verbose_name = _("بند في الطلب")
        verbose_name_plural = _("بنود الطلبات")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        """
        يحسب تكلفة هذا البند.
        """
        return self.price * self.quantity