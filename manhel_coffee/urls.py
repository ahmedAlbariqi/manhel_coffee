
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # توجيه الروابط إلى التطبيقات المخصصة
    # سنجعل الصفحة الرئيسية للموقع هي صفحة عرض المنتجات
    path('', include('apps.products.urls', namespace='products')),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('users/', include('apps.users.urls', namespace='users')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
]

# هذا الإعداد ضروري لعرض الصور والملفات المرفوعة في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)