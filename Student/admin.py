from django.contrib import admin
from .views import profile,home
from .models import *
# Register your models here.
admin.site.register(Favourites)
admin.site.register(videofeedback)
admin.site.register(Feedback)