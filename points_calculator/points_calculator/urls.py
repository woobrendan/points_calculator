from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('standings/', include('standings.urls')),
    path('drivers/', include('driver_standing.urls')),
    path('admin/', admin.site.urls),
]
