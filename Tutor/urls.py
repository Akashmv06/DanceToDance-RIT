from django.contrib import admin
from django.urls import path,include

from Administrator import views
from Tutor import views

app_name="Tutor"
urlpatterns = [
path('createplaylist',views.CreatePlayList,name="create-playlist"),
path('profile',views.Tutorprofile,name="profile"),
path('courses/',views.viewCourses,name="courses"),
path('courses/videos/<slug>/',views.viewVideo,name="coursevideos"),
path('courses/delete/<int:id>/',views.deleteVideo,name="deletevideos"),
path('0/',views.Back,name="back"),
]