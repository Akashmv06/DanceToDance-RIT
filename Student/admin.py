from django.contrib import admin
from .views import profile,home
from .models import Favourites
# Register your models here.
admin.site.register(Favourites)