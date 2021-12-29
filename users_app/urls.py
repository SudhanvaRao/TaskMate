from users_app import views as user_views
from django.urls import path,include
from django.http import HttpResponse
from django.contrib.auth import views as django_views


urlpatterns = [
    path('register', user_views.register, name='register'),
    path('login', django_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', django_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
