import json

from django.contrib.messages.context_processors import messages
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from .models import User


def load_user_page(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        user = User(username=post_data.get('username'),
                    password=post_data.get('password'),
                    Email=post_data.get('Email'),
                    phone=post_data.get('phone'),)
        try:
            user.save()
            return HttpResponse(json.dumps({'success': True, 'message': 'Signup is successful.'}))
        except IntegrityError as e:
            return HttpResponse(json.dumps({'success': False, 'message': e.__str__()}))

    else:
        return render(request, 'user/login_signup_page.html')

def login(request, username):
    post_data = json.loads(request.body.decode("utf-8"))
    user_password = User.objects.filter(username=username).values('password')

    if user_password:
        if post_data.get('password') == user_password[0].get('password'):
            return HttpResponse(json.dumps({'success': True, 'url': '/home_page/'+username}))
        else:
            return HttpResponse(json.dumps({'success': False, 'message': 'The password is wrong.'}))
    else:
        return HttpResponse(json.dumps({'success': False, 'message': 'The username is wrong.'}))


