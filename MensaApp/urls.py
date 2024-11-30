from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('activities/', views.activities, name='activities'),
    path('diary/', views.diary, name='diary'),
    path('mood/', views.mood, name='mood'),
    path("health-tracker/", views.health_tracker, name="health_tracker"),
    path("appointments/", views.appointments, name="appointments"),
    path("medications/", views.medications, name="medications"),
    path("notifications/", views.notifications, name="notifications"),
    path("mini_games/", views.mini_games, name="mini_games"),
    path("meditation_exercise/", views.meditation_exercise, name="meditation_exercise"),
    path("Selfcare/", views.Selfcare, name="Selfcare"),
    path('skill-building-exercises/', views.skill_building_exercises, name='SBE'),
]
