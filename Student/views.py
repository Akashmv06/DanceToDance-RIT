from Administrator.views import feedback
from django import http
from django.http.response import HttpResponseRedirect
import Student
from django.shortcuts import render,redirect,get_object_or_404
from Accounts.models import StudentModel,Subscription
from Administrator.models import News, Tutor,DanceCourses
from django.http import HttpResponse
from MasterEntry.models import ComplaintType, DanceCategory, DanceLevel,District
from Tutor.models import CourseVideo
from .models import Favourites, Feedback, RecentlyWatched, videofeedback
import stripe
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth import authenticate



# Create your views here.
def LevelData():
    recordSet=DanceLevel.objects.all()
    return recordSet

def CourseCat():
    rset=DanceCourses.objects.all()
    return rset
#home
def home(request):
    
    if request.session.has_key('student_id'):
        allNewsData=News.objects.all().order_by('-news_date')
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
    recordSet=LevelData()

    if request.method=="POST":
        Level=request.POST.get("level")
        courses=DanceCourses.objects.filter(course_level=Level).order_by('-course_name')
        return render(request,"Student/ViewCourses.html",{"courses":courses,"DanceLevel":recordSet})
    
    
    
    
    else:
        courses=DanceCourses.objects.all().order_by('-course_name')
    
        return render(request,"Student/ViewCourses.html",{"courses":courses,"DanceLevel":recordSet})

    
def viewVideo(request,slug):
    
    courses=DanceCourses.objects.get(slug=slug)
    
    allVideos=CourseVideo.objects.filter(cv_course_id=courses)
    # return HttpResponse(allVideos)
 
    return render(request,"Student/Coursevideo.html",{"allVideos":allVideos})


def AddFavourites(request,slug):
    

    if request.session.has_key('student_id'):
        
        
        # courses=DanceCourses.objects.get(slug=slug)
        # Videos=CourseVideo.objects.filter(cv_course_id=courses.id)
        #return HttpResponse(Videos)

        if request.method=="POST":  

            allVideos=Favourites()
            Vobj=CourseVideo.objects.get(id=slug)
            abc= Vobj.cv_course.slug
            allVideos.fvideo=Vobj
            allVideos.is_fav=True
            allVideos.fstudent=request.session['student_id']
            allVideos.save()

            #context={"allVideo":allVideos,"allVideo":Videos}
            return redirect("Student:viewvideo",slug=abc)
    else:
        return redirect("/accounts/login")
    


def viewFavourites(request):
    if request.session.has_key('student_id'):
        sid=request.session['student_id']
        allVideos=Favourites.objects.filter(fstudent=sid).order_by('-fdate')
        
        
        
        return render(request,"Student/favourites.html",{"allVideos":allVideos})
        
    else:
        return redirect("/accounts/login")

def subscription(request):
    if request.method == 'POST':
        membership = request.POST.get('membership' , 'MONTHLY')
        amount = 1000
        if membership == 'YEARLY':
            amount = 11000
        stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
        sid= request.session['student_id']
        s = get_object_or_404(StudentModel,id=sid)
        request.session['student_email']=s.student_email
        request.session['student_username']=s.student_username
        customer = stripe.Customer.create(
            
            
            email =request.session['student_email'],
			name=request.session['student_username'],
            source=request.POST['stripeToken']
			)
            
        charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Membership",   
		)
        
        print(charge['amount'])
        if charge['paid'] == True:
            sid=request.session['student_id']
            Student=get_object_or_404(StudentModel,id=sid)
            profile=Subscription()
            profile.subStudent=Student
            if charge['amount'] == 100000:
                
                profile.subscription_type = 'M'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(30)
                profile.pro_expiry_date = expiry
                profile.save()
                request.session['is_pro']=profile.is_pro
            elif charge['amount'] == 1100000:
                profile.subscription_type = 'Y'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(365)
                profile.pro_expiry_date = expiry
                profile.save()
                
                request.session['is_pro']=profile.is_pro
        
        print(charge)
        
        return redirect("/student/success/",{"profile":profile})
          
            
   
    return render(request, 'Student/Subscribe.html')
 

def charge(request):
    return render(request, 'Student/charge.html')
        
def videoSub(request,slug):
    sid=request.session['student_id']
    stu=StudentModel.objects.get(id=sid)
    sub=Subscription.objects.filter(subStudent_id=stu.id)
    if sub.exists():
        courses=DanceCourses.objects.filter(slug=slug).first()
        allVideos=CourseVideo.objects.filter(cv_course_id=courses)
        a=get_object_or_404(Subscription,subStudent_id=stu.id)
        request.session['is_pro']=a.is_pro
    
        context={"courses":courses,"allVideos":allVideos}
        return render(request,"Student/Coursevideo.html",context)
        
    else:
        return redirect("/student/subscription/")
        

def CategoryView(request):
  
        
        Category=DanceCategory.objects.all()
        return render(request,"Student/category.html",{"Category":Category})

def Coursecat(request,dancecategory_name):
    recordSet=LevelData()
    if request.method=="POST":
        Level=request.POST.get("level")
        Category=DanceCategory.objects.filter(dancecategory_name=dancecategory_name).first()
        courses=DanceCourses.objects.filter(course_dancecategory_id=Category,course_level=Level)
       
        return render(request,"Student/ViewCourses.html",{"courses":courses,"DanceLevel":recordSet})
    else:
        Category=DanceCategory.objects.filter(dancecategory_name=dancecategory_name).first()
        courses=DanceCourses.objects.filter(course_dancecategory_id=Category)
        context={"cat": Category,"courses":courses,"DanceLevel":recordSet}
    
    return render (request,"Student/Coursecategory.html",context)

def videoFeed(request,slug):
    
    if request.session.has_key('student_id'):
        
        
        if request.method=="POST":  

            sid=request.session['student_id']
            stu=StudentModel.objects.get(id=sid)
            allVideos=videofeedback()
            Vobj=CourseVideo.objects.get(id=slug)
            abc= Vobj.cv_course.slug
            allVideos.vfvideo=Vobj
            allVideos.vcontent=request.POST.get('content')
            allVideos.vfstudent=stu
            allVideos.save()
            #context={"allVideo":allVideos,"allVideo":Videos}
            return redirect("Student:viewvideo",slug=abc)
            # else:
            #     courses=DanceCourses.objects.filter(slug=slug).first()
            #     allVideos=CourseVideo.objects.filter(cv_course_id=courses)
            #     context={"allVideos":allVideos}
            #     return render(request,"Student/Coursevideo.html",context,{"Add":1})

            
    else:
        return redirect("/accounts/login")

def FeedBack(request):
    if request.session.has_key('student_id'):
        sid=request.session['student_id']
        stu=StudentModel.objects.get(id=sid)
        videofeed=videofeedback.objects.filter(vfstudent=stu).order_by('-vfsend')
        ctype=ComplaintType.objects.all()
        if request.method=='POST':
            a=Feedback()
            a.feedstudent=stu
            typeobj=ComplaintType.objects.get(id=request.POST.get("ftype"))
            a.feedtype=typeobj
            a.feedcontent=request.POST.get("fcontent")
            a.save()
            context={"videofeed":videofeed,"ctype":ctype}
            return redirect("/student/feedback/",context)
        else:
            context={"videofeed":videofeed,"ctype":ctype}
            return render(request,"Student/feedback.html",context)
    else:
        return redirect('/accounts/login/')

def deleteFavourites(request,id):
    if request.session.has_key('student_id'):
        fav=Favourites.objects.filter(id=id)
        if request.method=='POST':
            fav.delete()
            return redirect('/student/favourites/',{'fav':fav})

def updateDp(request,id):
    if request.session.has_key('student_id'):
        if request.method=='POST':
            students=StudentModel.objects.get(id=id)
            students.student_dp=request.FILES.get("dp")
            students.save()
            return redirect("/student/profile/")
    else:
        return redirect("/accounts/login/")
    
    
def updateprofile(request,id):
    if request.session.has_key('student_id'):
        if request.method=='POST':
            students=StudentModel.objects.get(id=id)
            dis=District.objects.all()
            students.student_name=request.POST.get("sname")
            students.student_contact=request.POST.get("scon")
            students.student_email=request.POST.get("semail")
            students.student_dob=request.POST.get("sdob")
           

            students.save()
            return redirect("/student/profile/",{"dis":dis})
    else:
        return redirect("/accounts/login/")
    
# def recentlywatched(request):
#     if request.session.has_key('student_id'):
#         sid=request.session['student_id']
#         stu=StudentModel.objects.get(id=sid)
#         vid=RecentlyWatched.objects.filter(watchstu=stu)
        
#         return HttpResponse(vid)

