from django.urls import path
from . import views

urlpatterns = [path('', views.load_home_page, name='home_page'),
               path('home_page/<str:username>', views.load_home_page, name='user_home_page'),]
