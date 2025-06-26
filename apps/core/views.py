from django.shortcuts import render

# Create your views here.

def home(request):
    """
    هذه الدالة (View) مسؤولة عن عرض الصفحة الرئيسية.
    هي تأخذ طلب المستخدم كمدخل (request)
    وتقوم بإرجاع قالب home.html كاستجابة.
    """
    return render(request, 'home.html')