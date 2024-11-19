from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('training.urls')),  # Connects to training app’s URLs
    path('login/', auth_views.LoginView.as_view(template_name='training/login.html'), name='login'),  # Specifies the template path
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]
