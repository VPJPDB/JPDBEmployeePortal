from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('handbook/', views.handbook, name='handbook'),
    path('static-debug/', views.static_debug_view, name='static_debug'),  # Debug route for static files
    path('logout/', views.logout_view, name='logout'),
    path('', views.login_view, name='login'),  # Login is the default route
]


