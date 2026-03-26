
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('projects.urls')),  # 👈 esto muestra la API
    path('admin/', admin.site.urls),
]