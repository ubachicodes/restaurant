from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
    # Other URL patterns for your application...
]
