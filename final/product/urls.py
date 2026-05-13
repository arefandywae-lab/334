from django.urls import path
from . import views

urlpatterns = [
    path('read', views.read_product),
    path('create', views.create_product),
    path('update/<int:id>', views.update_product),
    path('delete/<int:id>', views.delete_product),
]
