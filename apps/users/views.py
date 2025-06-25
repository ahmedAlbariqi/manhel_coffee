from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    return HttpResponse("ستكون هنا صفحة إنشاء حساب جديد")

def profile(request):
    return HttpResponse("ستكون هنا صفحة الملف الشخصي للمستخدم")