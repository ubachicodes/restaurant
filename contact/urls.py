from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_form, name='contact_form'),
    path('success/', views.success, name='success'),
]
