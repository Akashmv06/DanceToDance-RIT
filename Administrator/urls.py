from django.contrib import admin
from django.urls import path,include

from Administrator import views

app_name="Administrator"
urlpatterns = [
path('createnews/',views.CreateNews,name="create-news"),
path('tutors/',views.TutorAdd,name="tutors"),
path('courses/<int:id>',views.Courses,name="courses"),
path('courses/videos/<slug>',views.viewVideo,name="viewvideo"),
path('course/delete/<int:id>/',views.deleteCourse,name="deletecourse"),
path('tutors/delete/<int:id>/',views.deleteTutor,name="deletetutor"),
path('videofeed/',views.VideoFeed,name="videofeed"),
path('feedback/',views.feedback,name="feed"),
path('0/',views.goback,name="goback"),
path('approve-video/<int:id>',views.ApproveVideo,name='approve'),
path('waitlist/',views.waitlist,name='waitlist'),
# path('feedcateg/<int:id>',views.feedcateg,name="fcateg")
]