from django.shortcuts import render

def load_user_page(request):
    return render(request, 'user/login_signup_page.html')
# Create your views here.
