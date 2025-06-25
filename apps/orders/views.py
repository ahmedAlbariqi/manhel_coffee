from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cart_detail(request):
    return HttpResponse("ستكون هنا تفاصيل سلة الشراء")

def add_to_cart(request, product_id):
    return HttpResponse(f"سيتم هنا إضافة المنتج رقم {product_id} للسلة")

def checkout(request):
    return HttpResponse("ستكون هنا صفحة الدفع")