from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('contact/', views.contact_form, name='contact_form'),  # Use the view function from the imported views module
    path('success/', views.success, name='success'),
]

