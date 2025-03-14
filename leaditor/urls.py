# leaditor/urls.py
from django.contrib import admin
from django.urls import path, include
from leads import views  # Import views to access home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add a home view for the root URL
]
