
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
]

from django.urls import path
from .views import register_view, edit_profile_view, change_password_view

urlpatterns += [
    path('register/', register_view, name='register'),
    path('edit_profile/', edit_profile_view, name='edit_profile'),
    path('change_password/', change_password_view, name='change_password'),
]
