from django.urls import path

from . import views

app_name = 'standing'

urlpatterns = [
    path('drivers/', views.drivers_standing, name="drivers")
]
