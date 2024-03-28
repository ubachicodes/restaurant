from django.urls import path
from . import views


app_name = 'reservation'

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
]