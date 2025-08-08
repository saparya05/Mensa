from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('activities/', views.activities, name='activities'),
    path('diary/', views.diary, name='diary'),
    path("health-tracker/", views.health_tracker, name="health_tracker"),
    path("appointments/", views.appointments, name="appointments"),
    path("medications/", views.medications, name="medications"),
    path("notifications/", views.notifications, name="notifications"),
    path("mini_games/", views.mini_games, name="mini_games"),
    path('skill-building-exercises/', views.skill_building_exercises, name='SBE'),
    path('meditation-exercise/', views.static_page_view, {'page_key': 'meditation_exercise'}, name='meditation_exercise'),
    path('selfcare/', views.static_page_view, {'page_key': 'selfcare'}, name='selfcare'),
]
