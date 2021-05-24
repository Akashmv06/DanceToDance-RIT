from django.contrib import admin
from django.urls import path,include

from Administrator import views
from Tutor import views

app_name="Tutor"
urlpatterns = [
path('createplaylist',views.CreatePlayList,name="create-playlist"),
path('profile',views.Tutorprofile,name="profile"),
]