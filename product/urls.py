from django.urls import path
from . import views

urlpatterns = [path("search/<int:category_id>", views.find_product_with_category, name="find_product_with_category"),
               path("product_detail/<int:product_id>", views.show_product_details, name="show_product_details"),
               path("search/<str:product_name>", views.find_product_with_name, name="find_product_with_name"),
               ]