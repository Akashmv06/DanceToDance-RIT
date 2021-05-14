from django.contrib import admin
from django.urls import path,include

from Administrator import views

app_name="Administrator"
urlpatterns = [
path('createnews',views.CreateNews,name="create-news"),
]