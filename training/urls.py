from django.urls import path
from . import views  # Import views from the current app
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('handbook/', views.handbook, name='handbook'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
]

