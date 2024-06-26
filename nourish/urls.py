from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # URL for admins
    path('', include('home.urls')),    # URL for the home page
    path('meals/', include('meals.urls')),  # URL for the menu page
    path('reservation/', include('reservation.urls')),  # URL for the reservation page
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
