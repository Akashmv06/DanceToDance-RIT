from Accounts.models import adminmodel
from django.shortcuts import redirect, render
from MasterEntry.models import ComplaintType, DanceCategory, DanceLevel, Designation, District, NewsType
from .models import DanceCourses, News, Tutor
from django.http import HttpResponse
from django.contrib.auth.models import User
from Tutor.models import CourseVideo
from Student.models import videofeedback,Feedback

def NewstypeSelect():
    NewsTypeRecords=NewsType.objects.all()
    return NewsTypeRecords

def CreateNews(request):
    #return render(request,"Administrator/NewsManagement.html")
    NewsTypeRecords=NewstypeSelect()
    news=News.objects.all()
    loc=District.objects.all()
    if request.method == 'POST':
        p=News()
        p.news_title= request.POST.get("ntitle")
        p.news_content= request.POST.get("ncontent")
        NewsTypeObj=NewsType.objects.get(id=request.POST.get("ntype"))
        p.news_newstype=NewsTypeObj
        locobj=District.objects.get(id=request.POST.get("nloc"))
        p.news_poster=request.FILES.get("nposter")
        p.news_loc=locobj
        p.news_date=request.POST.get("ndate")
        p.save()
        return redirect("/administrator/createnews/",{"news":news,"loc":loc})
    else:
        return render(request,"Administrator/NewsManagement.html",{'NewsTypeRecords':NewsTypeRecords,"news":news,"loc":loc})

def TutorAdd(request):
    if request.session.has_key('admin_id'):
        tutor=Tutor.objects.all()
        des=Designation.objects.all()
        cat=DanceCategory.objects.all()
        dis=District.objects.all()
        if request.method=='POST':
            a=Tutor()
            a.tutor_name=request.POST.get("tname")
            a.tutor_contact=request.POST.get("tnum")
            a.tutor_email=request.POST.get("temail")
            a.tutor_gender=request.POST.get("tgender")
            a.tutor_dob=request.POST.get("tdob")
            a.tutor_username=request.POST.get("tusername")
            a.tutor_password=request.POST.get("tpassword")
            a.tutor_photo=request.FILES.get("tphoto")
            desObj=Designation.objects.get(id=request.POST.get("tdesign"))
            catObj=DanceCategory.objects.get(id=request.POST.get("tcat"))
            disObj=District.objects.get(id=request.POST.get("tdistrict"))
            a.tutor_designation=desObj
            a.tutor_dancecategory=catObj
            a.tutor_district=disObj
            a.save()
            context={"des":des,"cat":cat,"did":dis,"Tutor":tutor}
            return redirect('/administrator/tutors/',context)
        else:
            context={"des":des,"cat":cat,"dis":dis,"Tutor":tutor}
            return render(request,"Administrator/Tutor.html",context)
    else:
        return redirect("/accounts/login/")
    

def Courses(request,id):
    if request.session.has_key('admin_id'):
        Tut=Tutor.objects.filter(id=id).first()
        courses=DanceCourses.objects.filter(course_tutor_id=Tut)

        cat=DanceCategory.objects.all()
        level=DanceLevel.objects.all()
        if request.method=="POST":

            a=DanceCourses()
            a.course_tutor=Tut
            a.course_name=request.POST.get("cname")
            a.course_photo=request.FILES.get("cphoto")
            a.course_description=request.POST.get("cdes")
            a.is_premium=request.POST.get("ispre")
            catObj=DanceCategory.objects.get(id=request.POST.get("ccat"))
            levObj=DanceLevel.objects.get(id=request.POST.get("clev"))
            a.course_dancecategory=catObj
            a.course_level=levObj
            a.save()
            context={"cat":cat,"level":level,"Tutor":Tut,"courses":courses}
            return redirect('Administrator:courses',id=id)
        else:
            context={"cat":cat,"level":level,"Tutor":Tut,"courses":courses}
            return render(request,"Administrator/courses.html",context)
    else:
        return redirect("/accounts/login/")

def viewVideo(request,slug):
    courses=DanceCourses.objects.filter(slug=slug).first()
    allVideos=CourseVideo.objects.filter(cv_course_id=courses)
    context={"courses":courses,"allVideos":allVideos}
    if request.method=="POST":
        allVideos=CourseVideo.objects.get(id=request.POST.get('vid'))
        if allVideos.cv_approve is False:
            allVideos.cv_approve=True
            allVideos.save()
            return render(request,"Administrator/Coursevideo.html",context)   
        else:
            allVideos=CourseVideo.objects.get(id=request.POST.get('vid'))
            allVideos.cv_approve=False
            allVideos.save()
            return render(request,"Administrator/Coursevideo.html",context)   
    else:
        return render(request,"Administrator/Coursevideo.html",context)  
            
def deleteCourse(request,id):
    if request.session.has_key('admin_id'):
        if request.method=='POST':
            courses=DanceCourses.objects.filter(id=id)
            courses.delete()
            return redirect('Administrator:goback')

def deleteTutor(request,id):
    if request.session.has_key('admin_id'):
        if request.method=='POST':
            tutor=Tutor.objects.filter(id=id)
            tutor.delete()
            context={"Tutor":tutor}
            return redirect('Administrator:tutors')
            
def VideoFeed(request):
    if request.session.has_key('admin_id'):
        videofeed=videofeedback.objects.all().order_by('-vfsend')
        if request.method=="POST":
            context={"videofeed":videofeed}
            return render(request,"Administrator/videofeed.html",context)
        else:
            return redirect("/administrator/feedback")

def feedback(request):
    if request.session.has_key('admin_id'):
        feed=Feedback.objects.all().order_by('-feedsend')
        ctype=ComplaintType.objects.all()
        if request.method=='POST':
            return render(request,"Administrator/feedback.html",{"feed":feed,"ctype":ctype})
        else:
            return render(request,"Administrator/feedback.html",{"feed":feed,"ctype":ctype})
    else:
        return redirect("/accounts/login/")
    
def goback(request):
    return render(request,"Administrator/Back.html")   
def waitlist(request):
    videos=CourseVideo.objects.filter(cv_approve=False)
    return render(request,'Administrator/waitlist.html',{'videos':videos})
def ApproveVideo(request,id):
    if request.session.has_key('admin_id'):
        
        videos=CourseVideo.objects.filter(cv_approve=False)
        if request.method=="POST":
            allvideos=CourseVideo.objects.get(id=id)
            allvideos.cv_approve=True
            allvideos.save()
            context={'videos':videos}
            return redirect('/administrator/waitlist/',context)
        
    else:
        return redirect("/accounts/login/")
def feedcateg(request,id):
    categ=Feedback.objects.filter(feedtype=id)
    return redirect('Administrator:feed',{'categ':categ})