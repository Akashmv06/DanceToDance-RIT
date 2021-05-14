
from django.db.models.fields import AutoField, BigAutoField
from .models import StudentModel
from django.http import HttpResponse
from MasterEntry.models import District
from django.contrib import messages
from django.shortcuts import render


# Create your views here.
def selectAllDistrict():
    DistrictRecords=District.objects.all()
    return DistrictRecords


#def accfun(request):
    #posts=StudentModel.objects.all()
    #return render (request,"Accounts/StudentRegistration.html",{'posts':posts})

def studentRegister(request):
    DistrictRecords=selectAllDistrict()
    if request.method == 'POST':
        p=StudentModel()
        p.student_name= request.POST.get("sname")
        p.student_contact= request.POST.get("snum")
        DistrictObj=District.objects.get(id=request.POST.get("dist"))
        p.student_district=DistrictObj
            

        p.student_dob= request.POST.get("dob")
        p.student_dp= request.POST.get("filename")
        p.student_email= request.POST.get("email")
        p.student_gender= request.POST.get("gender")
        p.student_password= request.POST.get("password")
        
        p.student_reenterpassword= request.POST.get("repeatPassword")
        p.student_username=request.POST.get("username")
        p.save()
        messages.success(request, 'created successfully.')
          
        return render(request, "Accounts/StudentRegistration.html",{'DistrictRecords':DistrictRecords})  

    else:
        return render(request, "Accounts/StudentRegistration.html",{'DistrictRecords':DistrictRecords})


        #login
def login(request):
    if request.method=='POST':
        StudentDataCount=StudentModel.objects.filter(student_username=request.POST.get("username"),student_password=request.POST.get("password")).count()
        if StudentDataCount>0:
            StudendentObj = get_object_or_404(StudentModel, tstudent_username=request.POST.get("username"),student_password=request.POST.get("Password"))
            request.session["student_id"]=StudendentObj.student_id
            request.session["student_name"]=StudendentObj.student_name
            return redirect("/accounts/homepage")
        else: 
            return HttpResponse("Invalid Data")
    return render(request,"Accounts/Login.html",{})

#home
def home(request):
    return render(request,"Accounts/Home.html",{})