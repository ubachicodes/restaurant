from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    # Add more paths as needed for additional about page views
]