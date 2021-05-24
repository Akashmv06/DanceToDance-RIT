from Tutor.models import CourseVideo
from Administrator.models import Tutor
from django.shortcuts import render,redirect
from MasterEntry.models import DanceCategory

# Create your views here.
def CreatePlayList(request):
    pass
    

def Tutorprofile(request):
    if request.session.has_key('tutor_id'):
        tid = request.session['tutor_id']
        tutors=Tutor.objects.filter(id=tid)
        return render(request,"Tutor/Viewprofile.html",{'tutors':tutors})
    else:
        return redirect("/accounts/login")

def CategorySelect():
    CategoryRecords=DanceCategory.objects.all()
    return CategoryRecords

#dancevideoupload
def UploadVideo(request):
   pass
    