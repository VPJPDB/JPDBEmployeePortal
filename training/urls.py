from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('training.urls')),  # Includes URLs from the training app
    path('login/', auth_views.LoginView.as_view(template_name='training/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('register/', views.register, name='register'),  # Registration page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
]

