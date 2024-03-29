from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
    path('api/tables', views.tables_api, name='tables_api'),
]
