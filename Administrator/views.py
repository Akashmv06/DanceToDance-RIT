from django.shortcuts import redirect, render
from MasterEntry.models import DanceCategory, Designation, District, NewsType
from .models import News, Tutor
from django.http import HttpResponse
from django.contrib.auth.models import User

def NewstypeSelect():
    NewsTypeRecords=NewsType.objects.all()
    return NewsTypeRecords

def CreateNews(request):
    #return render(request,"Administrator/NewsManagement.html")
    NewsTypeRecords=NewstypeSelect()
    news=News.objects.all()
    if request.method == 'POST':
        p=News()
        p.news_title= request.POST.get("ntitle")
        p.news_content= request.POST.get("ncontent")
        NewsTypeObj=NewsType.objects.get(id=request.POST.get("ntype"))
        p.news_newstype=NewsTypeObj
        p.news_poster=request.FILES.get("nposter")
        p.save()
        return redirect("/administrator/createnews/",{"news":news})
    else:
        return render(request,"Administrator/NewsManagement.html",{'NewsTypeRecords':NewsTypeRecords,"news":news})

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
        
