from django.urls import path

from . import views

app_name = 'drivers'

urlpatterns = [
    path('drivers/<str:series>/', views.drivers_standing, name="drivers")
]
