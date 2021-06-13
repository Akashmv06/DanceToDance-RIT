
from django.db.models.fields import AutoField, BigAutoField
from django.urls.conf import include
from .models import StudentModel,Subscription, adminmodel
from Administrator.models import Tutor
from django.http import HttpResponse
from MasterEntry.models import District, SubscriptionType
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
import stripe
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth.models import User




# Create your views here.
def selectAllDistrict():
    DistrictRecords=District.objects.all()
    return DistrictRecords


#def accfun(request):
    #posts=StudentModel.objects.all()
    #return render (request,"Accounts/StudentRegistration.html",{'posts':posts})

def studentRegister(request):
    if request.session.has_key('student_id'):
        return redirect("/student/home")
    elif request.session.has_key('tutor_id'):
        return redirect("/tutor/profile")
    elif request.session.has_key('admin_id'):
        return redirect('/administrator/createnews/')
    DistrictRecords=selectAllDistrict()
    if request.method == 'POST':
        p=StudentModel()
        p.student_name= request.POST.get("sname")
        p.student_contact= request.POST.get("snum")
        DistrictObj=District.objects.get(id=request.POST.get("dist"))
        p.student_district=DistrictObj
            

        p.student_dob= request.POST.get("dob")
        p.student_dp= request.FILES.get("filename")
        p.student_email= request.POST.get("email")
        p.student_gender= request.POST.get("gender")
        p.student_password= request.POST.get("password")
        
        p.student_reenterpassword= request.POST.get("repeatPassword")
        p.student_username=request.POST.get("username")
        p.save()
        if request.session.has_key('student_id'):
            return redirect("/student/home")
        elif request.session.has_key('tutor_id'):
            return redirect("/tutor/profile")
        StudentObj = get_object_or_404(StudentModel, student_username=request.POST.get("username"),student_password=request.POST.get("password"))
        request.session["student_id"]=StudentObj.id
        request.session["student_name"]=StudentObj.student_name
        request.session["student_dp"]=StudentObj.student_dp.url

        #messages.success(request, 'created successfully.')
          
        #return render(request, "Accounts/StudentRegistration.html",{'DistrictRecords':DistrictRecords})  
        return redirect("/student/home")

    else:
        return render(request, "Accounts/StudentRegistration.html",{'DistrictRecords':DistrictRecords})



        #login

def login(request):
    if request.session.has_key('student_id'):
        return redirect("/student/home")
        
    elif request.session.has_key('tutor_id'):
        return redirect("/tutor/profile")
    elif request.session.has_key('admin_id'):
        return redirect("/administrator/createnews/")
    
    else:
        if request.method=='POST':
            StudentDataCount=StudentModel.objects.filter(student_username=request.POST.get("username"),student_password=request.POST.get("password")).count()
            TutorDataCount=Tutor.objects.filter(tutor_username=request.POST.get("username"),tutor_password=request.POST.get("password")).count()
            AdminDataCount=adminmodel.objects.filter(Admin_username=request.POST.get("username"),Admin_password=request.POST.get("password")).count()
            if StudentDataCount>0:
                StudentObj = get_object_or_404(StudentModel, student_username=request.POST.get("username"),student_password=request.POST.get("password"))
                request.session["student_id"]=StudentObj.id
                request.session["student_name"]=StudentObj.student_name
                request.session["student_dp"]=StudentObj.student_dp.url
                p=StudentModel.objects.all()
                sub=Subscription.objects.filter(subStudent=StudentObj)
                if sub.exists():
                    a=get_object_or_404(Subscription,subStudent=StudentObj)
                    request.session['is_pro']=a.is_pro
                
                return redirect("/student/home",{'p':p})
            elif TutorDataCount>0:
                Tutorobj = get_object_or_404(Tutor,tutor_username=request.POST.get("username"),tutor_password=request.POST.get("password"))
                request.session["tutor_id"]=Tutorobj.id
                request.session["tutor_name"]=Tutorobj.tutor_name
                request.session["tutor_photo"]=Tutorobj.tutor_photo.url
                return redirect("/tutor/profile")
            elif AdminDataCount>0:
                AdminObj=get_object_or_404(adminmodel,Admin_username=request.POST.get("username"),Admin_password=request.POST.get("password"))
                request.session["admin_id"]=AdminObj.id
                request.session["admin_name"]=AdminObj.Admin_username
                return redirect("/administrator/createnews")
            else: 
               return render(request,"Accounts/Login.html",{'fail':1})
        return render(request,"Accounts/Login.html",{})


def logout(request):
    request.session.flush()
    return redirect("/accounts/login")
    
