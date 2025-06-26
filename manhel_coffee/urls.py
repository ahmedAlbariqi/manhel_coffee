from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # =============================================================
    # === التعديلات هنا بناءً على الخيار الأول (الموصى به) ===
    # =============================================================

    # 1. تم توجيه المسار الرئيسي '' إلى تطبيق core لعرض الصفحة الرئيسية
    path('', include('apps.core.urls', namespace='core')),
    
    # 2. تم تغيير مسار المنتجات ليصبح 'products/'
    path('products/', include('apps.products.urls', namespace='products')),
    
    # =============================================================

    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('users/', include('apps.users.urls', namespace='users')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
]

# هذا الإعداد ضروري لعرض الصور والملفات المرفوعة في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)