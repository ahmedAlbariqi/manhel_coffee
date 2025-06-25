from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # مثال: رابط لعرض سلة الشراء
    path('cart/', views.cart_detail, name='cart_detail'),
    
    # مثال: رابط لإضافة منتج إلى السلة
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    # مثال: رابط لعملية الدفع
    path('checkout/', views.checkout, name='checkout'),
]