from django.contrib import admin
from django.urls import path,include


from Student import views

app_name="Student"
urlpatterns = [

path('home/',views.home,name="home"),
path('profile/',views.profile,name="profile"),
path('changepass/',views.ChangePassword,name="changepass"),
path('courses/',views.ViewCourses,name="viewcourse"),
]