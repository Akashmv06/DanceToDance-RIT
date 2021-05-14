from django.contrib import admin
from django.urls import path,include

from Administrator import views

app_name="Tutor"
urlpatterns = [
path('/createplaylist',views.CreatePlayList,name="create-playlist"),
]