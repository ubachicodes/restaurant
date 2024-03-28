from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),  # Updated to 'user_login'
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout, name="logout")
]
