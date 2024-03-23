"""
URL configuration for nourish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls), # URL for admins
    path('', include('home.urls')),  # URL for the home page
    path('about/', views.about, name='about'),  # URL for the about page
    path('meals/', views.menu, name='meals'),  # URL for the menu page
    path('blog/', views.blog, name='blog'),  # URL for the blog page
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),  # URL for individual blog post detail page
    path('reservation/', views.reservation, name='reservation'),  # URL for the reservation page
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
