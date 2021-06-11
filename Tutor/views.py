from Student.models import videofeedback
from django.http.response import HttpResponse, HttpResponseRedirect
from Tutor.models import CourseVideo
from Administrator.models import DanceCourses, Tutor
from django.shortcuts import render,redirect
from MasterEntry.models import DanceCategory, District

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

def courseselect():
    courses=DanceCourses.objects.all()
    return courses

#dancevideoupload
def UploadVideo(request):
    courses=courseselect()
    if request.method == 'POST':
        courses=courseselect()
        v=CourseVideo()
        v.cv_title= request.POST.get("vtitle")
        v.cv_thumbnail= request.FILES.get("vthumb")
        v.cv_video=request.FILES.get("vvideo")
        CourseObj=DanceCourses.objects.get(id=request.POST.get("course"))
        v.cv_course=CourseObj
        v.save()
        return render(request,"Tutor/CourseVideos.html",{'courses':courses})
       
    else:
        return render(request,"Tutor/CourseVideos.html",{'courses':courses})

def viewCourses(request):
    if request.session.has_key('tutor_id'):
        tid = request.session['tutor_id']
        courses=DanceCourses.objects.filter(course_tutor_id=tid)
        context={"courses":courses}
        return render(request,"Tutor/Courses.html",context)
    else:
        return redirect("/accounts/login")

def selectvideo():
    cid=DanceCourses.objects.all()

    return cid


def viewVideo(request,slug):
    courses=DanceCourses.objects.filter(slug=slug).first()
    allVideos=CourseVideo.objects.filter(cv_course_id=courses)
    
    context={"courses":courses,"allVideos":allVideos}
    if request.method == 'POST':
    
        p=CourseVideo()
        p.cv_title= request.POST.get("vtitle")
        p.cv_video= request.FILES.get("vvideo")
        p.cv_thumbnail= request.FILES.get("vthumb")
        CourseObj=DanceCourses.objects.get(id=request.POST.get("vcourse"))
        p.cv_course=CourseObj
        p.save()
        return render(request,"Tutor/Coursevideos.html",{'allVideos':allVideos,"courses":courses,'Update':1})
    return render(request,"Tutor/Coursevideos.html",context)

def deleteVideo(request,id):
    allVideos=CourseVideo.objects.filter(id=id)
    
    if request.session.has_key('tutor_id'):
        if request.method=="POST":
            allVideos.delete()
            
            return redirect("/tutor/0/",{"allVideos":allVideos})
    else:
        return redirect("/accounts/login")

def Back(request):
    return render(request,"Tutor/back.html")

def updateDp(request,id):
    if request.session.has_key('tutor_id'):
        if request.method=='POST':
            tutors=Tutor.objects.get(id=id)
            tutors.tutor_photo=request.FILES.get("dp")
            tutors.save()
            return redirect("/tutor/profile/")
    else:
        return redirect("/accounts/login/")
        
def updateProfile(request,id):
    if request.session.has_key('tutor_id'):
        if request.method=='POST':
            tutors=Tutor.objects.get(id=id)
            dis=District.objects.all()
            tutors.tutor_name=request.POST.get("tname")
            tutors.tutor_contact=request.POST.get("tcon")
            tutors.tutors_email=request.POST.get("temail")
            tutors.tutors_dob=request.POST.get("tdob")
            disobj=District.objects.get(id=request.POST.get("tdis"))
            tutors.tutor_district=disobj
            tutors.save()
            return redirect("/tutor/profile/",{"dis":dis})
    else:
        return redirect("/accounts/login/")

def videofeed(request,id):
    allVideos=CourseVideo.objects.filter(id=id).first()
    feed=videofeedback.objects.filter(vfvideo=allVideos)
    return render(request,"Tutor/videofeed.html",{"feed":feed,"allVideos":allVideos})
             


            
    