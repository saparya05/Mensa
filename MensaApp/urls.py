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
]
