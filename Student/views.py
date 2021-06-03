import Student
from django.shortcuts import render,redirect,get_object_or_404
from Accounts.models import StudentModel
from Administrator.models import News, Tutor,DanceCourses
from django.http import HttpResponse
from MasterEntry.models import DanceCategory
from Tutor.models import CourseVideo
from .models import Favourites


# Create your views here.
def DanceCategoryData():
    recordSet=DanceCategory.objects.all()
    return recordSet

def CourseCat():
    rset=DanceCourses.objects.all()
    return rset
#home
def home(request):
    
    if request.session.has_key('student_id'):
        allNewsData=News.objects.all()
        return render(request,"Student/Home.html",{'allnewsdata':allNewsData})
            
    else:
        return redirect("/accounts/login")


def profile(request):
    if request.session.has_key('student_id'):
        sid = request.session['student_id']
        students=StudentModel.objects.filter(id=sid)
        return render(request,"Student/profile.html",{'students':students})
    else:
        return redirect("/accounts/login")

def ChangePassword(request):
    if request.session.has_key('student_id'):
        if request.method=='POST':
            currentPassword=request.POST.get("txtCurrentPassword")
            newPassword=request.POST.get("txtNewPassword")
            confirmPassword=request.POST.get("txtConfirmNewPassword")
            StudentData=StudentModel.objects.filter(student_password=currentPassword).count()
            if StudentData>0:
                if newPassword==confirmPassword:
                    Studentobj=StudentModel.objects.get(student_password=currentPassword)
                    Studentobj.student_password=newPassword
                    Studentobj.save()
                    return redirect("/student/profile")
                else:
                    return HttpResponse("Password Mismatch")
            else:
                return HttpResponse("Current password Does not Exist!!!")
        return render(request,"Student/Changepassword.html",{})
    else:
        return redirect("/accounts/login")

def ViewCourses(request):
    #recordSet=DanceCategoryData()
    #if request.method=="POST":
        #selectedCourseCategory=request.POST.get("slcTCourseCategory")
        #allCoursesData=DanceCourses.objects.filter(course_dancecategory=selectedCourseCategory)
        #return render(request,"Student/ViewCourses.html",{"allCoursesData":allCoursesData,"DanceCategories":recordSet})
    #else:
    
    courses=DanceCourses.objects.all()
    context={"courses":courses}
    return render(request,"Student/ViewCourses.html",context)

    
def viewVideo(request,slug):
    courses=DanceCourses.objects.filter(slug=slug).first()
    allVideos=CourseVideo.objects.filter(cv_course_id=courses)
    
    context={"courses":courses,"allVideos":allVideos}
    return render(request,"Student/Coursevideo.html",context)

def AddFavourites(request,slug):

    if request.session.has_key('student_id'):
        allVideos=CourseVideo.objects.filter(slug=slug)
        
        if request.method=='POST':
            
            a=Favourites()
            a.fstudent=request.session['student_id']
            VObj=CourseVideo.objects.get(id=request.POST.get("vi"))
            a.fvideo=VObj
            a.save()
            context={"allvideos":allVideos}
            return redirect ("courses/videos/",context)
            
    else:
        return redirect("/accounts/login")
    


def viewFavourites(request):
    if request.session.has_key('student_id'):
        sid=request.session['student_id']
        fav=Favourites.objects.filter(fstudent=sid)
        return render(request,"Student/favourites.html",{"fav":fav})
    else:
        return redirect("/accounts/login")

