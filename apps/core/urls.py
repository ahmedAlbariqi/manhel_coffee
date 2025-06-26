from django.urls import path
from . import views

app_name = 'core'  # اسم نطاق للتطبيق لتجنب تضارب الأسماء مستقبلاً

urlpatterns = [
    # المسار الفارغ '' يعني الرابط الرئيسي للتطبيق
    # name='home' هو اسم مميز لهذا المسار سنستخدمه في القوالب لاحقًا
    path('', views.home, name='home'),
]