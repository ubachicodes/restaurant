from django.urls import path
from . import views


urlpatterns = [
    path('', views.meal_list),
    path('<slug:slug>', views.meal_detail, name='meal_detail'),
]