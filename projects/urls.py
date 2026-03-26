from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("API funcionando 🚀")

urlpatterns = [
    path('', home),  # 👈 ESTO ARREGLA EL ERROR 500
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
]
