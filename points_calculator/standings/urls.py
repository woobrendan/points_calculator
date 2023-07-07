from django.urls import path

from . import views

app_name = 'standing'

urlpatterns = [
    path('drivers/<str:series>/', views.drivers_standing, name="drivers"),
    path('team/<str:series>/', views.team_standing, name="team"),
    path('new/', views.new_result, name="new")
]
