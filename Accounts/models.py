
from django.db import models
from MasterEntry.models import District


class StudentModel(models.Model):
    student_name=models.CharField("Name",max_length=20,null=False)
    student_contact=models.CharField("Contact",max_length=10,null=False)
    student_email=models.EmailField("Email",unique=True,max_length=50,null=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    student_gender = models.CharField("Gender",max_length=20, choices=GENDER_CHOICES,null=False)
    student_dob=models.DateField("Date of birth",null=False)
    student_username=models.CharField("Username",max_length=20,unique=True,null=False)
    student_password=models.CharField("Password",max_length=20,unique=True,null=False) 
    student_reenterpassword=models.CharField("Re-enter password",max_length=20,unique=True,null=False)
    student_district=models.ForeignKey(District,on_delete=models.CASCADE,null=True,verbose_name="District")
    
    student_regdate=models.DateField("student_regdate",auto_now_add=True,null=False)
    student_dp=models.ImageField("Profile picture",upload_to='profile',null=False)
   
    def __str__(self):
        return self.student_username
        
       
        



