from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('cart/', views.view, name='view'),
    path('add/<int:product_id>/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
