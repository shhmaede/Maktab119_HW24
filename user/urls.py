from . import views
from django.urls import path

urlpatterns = [path("user_page/", views.load_user_page, name="user_page")]