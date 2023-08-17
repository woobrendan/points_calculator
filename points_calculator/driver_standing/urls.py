from django.urls import path

from . import views

app_name = 'drivers'

urlpatterns = [
    path('<str:series>/', views.drivers_standing, name="standing")
]
