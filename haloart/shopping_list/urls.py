from django.urls import path
from . import views


app_name = 'shopping_list'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
