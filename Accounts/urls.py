from django.contrib import admin
from django.urls import path,include

from Accounts import views

app_name="Accounts"
urlpatterns = [
path('registerstudent/',views.studentRegister,name="student-register"),
path('login/',views.login,name="login"),
path('logout/',views.logout,name="logout"),


#path('profile',views.accfun,name="profile"),

]