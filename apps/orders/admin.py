from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    """
    لعرض بنود الطلب بشكل جدولي داخل صفحة الطلب الرئيسي.
    """
    model = OrderItem
    # الحقول التي ستظهر للقراءة فقط، لأن بنود الطلب لا يجب تعديلها بعد إنشائه
    readonly_fields = ('product', 'price', 'quantity', 'get_cost')
    extra = 0 # عدم إظهار حقول فارغة لإضافة بنود جديدة
    can_delete = False # منع حذف البنود من الطلب

    def get_cost(self, obj):
        return obj.get_cost()
    get_cost.short_description = 'التكلفة'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    تخصيص عرض الطلبات في لوحة التحكم.
    """
    list_display = ['id', 'user', 'first_name', 'last_name', 'paid', 'status', 'created_at', 'get_total_cost']
    list_filter = ('status', 'paid', 'created_at')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'user__username')
    # معظم الحقول للقراءة فقط لأن الطلب هو سجل تاريخي لا يجب تعديله
    readonly_fields = (
        'user', 'first_name', 'last_name', 'email', 'phone', 'address', 'city', 
        'created_at', 'updated_at', 'get_total_cost'
    )
    inlines = [OrderItemInline] # تضمين بنود الطلب في صفحة الطلب

    # لمنع القدرة على إضافة طلبات جديدة من لوحة التحكم مباشرة
    # لأن الطلبات يجب أن تأتي من عملية شراء فعلية
    def has_add_permission(self, request):
        return False