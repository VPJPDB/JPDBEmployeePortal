from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('training.urls')),  # Includes all URLs from the training app
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
]
