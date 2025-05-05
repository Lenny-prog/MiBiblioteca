from django.contrib import admin
from django.urls import path, include
from .views import bienvenida

urlpatterns = [
    path('', bienvenida, name='home'),
    path('admin/', admin.site.urls),
    path('libros/', include('libreria.urls')),
    path('', include('accounts.urls')),
]

