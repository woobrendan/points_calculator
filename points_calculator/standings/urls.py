from django.urls import path

from . import views

app_name = 'standing'

urlpatterns = [
    path('team/<str:series>/', views.team_standing, name="team"),
    path('manufacturer/<str:series>/', views.manuf_standing, name="manufacturer"),
    path('new/', views.new_result, name="new")
]
