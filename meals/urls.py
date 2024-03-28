from django.urls import path
from . import views


urlpatterns = [
    path('meals/', views.meal_list, name='meals'),
    path('<slug:slug>/', views.meal_detail, name='meal_detail'),  # URL for displaying meal details
]

