from django.urls import path
from . import views

urlpatterns = [path('', views.load_home_page, name='home_page')]
