from django.contrib import admin
from django.urls import path,include


from Student import views

app_name="Student"
urlpatterns = [

path('home/',views.home,name="home"),
path('profile/',views.profile,name="profile"),
path('changepass/',views.ChangePassword,name="changepass"),
path('courses/',views.ViewCourses,name="viewcourse"),
path('courses/videos/<slug>/',views.viewVideo,name="viewvideo"),
path('subs/<slug>',views.videoSub,name="subvideos"),
path('course/videos/<slug>/',views.AddFavourites,name="favourites"),
path('subscription/',views.subscription,name="subscription"),
path('success/',views.charge,name="charge"),
path("favourites/",views.viewFavourites,name="viewfavourites"),
path("coursecategories/",views.CategoryView,name="categories"),
path("coursecategories/<dancecategory_name>/",views.Coursecat,name="coursecat"),
path("comment/video/<slug>/",views.videoFeed,name="videofeed"),
path('feedback/',views.FeedBack,name="feedback"),
path('favourites/0/<int:id>',views.deleteFavourites,name="deletefav"),
path('updatedp/<int:id>',views.updateDp,name="updatedp"),
path('updateprofile/<int:id>',views.updateprofile,name="updateprofile"),
]