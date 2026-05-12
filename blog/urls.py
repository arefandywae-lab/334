# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ตั้งค่าหน้าแรกเป็น Login (Standalone)
    path('', views.login_full_view, name='login_full'),
    
    # ย้าย Blog ไปที่ /blog/
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    
    # Auth (Standard - Extends base.html)
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Auth (Standalone - Full Page)
    path('register-full/', views.register_full_view, name='register_full'),
]