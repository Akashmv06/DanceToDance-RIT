
from django.db import models
from MasterEntry.models import District
from django_countries.fields import CountryField


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
    student_country=CountryField()
    student_regdate=models.DateField("student_regdate",auto_now_add=True,null=False)
    student_dp=models.ImageField("Profile picture",upload_to='profile')
   
    def __str__(self):
        return self.student_username
        
SUBSCRIPTION = (
    ('F' , 'FREE'),
    ('M' , 'MONTHLY'),
    ('Y' , 'YEARLY'),
    )


class Subscription(models.Model):
    subStudent =models.ForeignKey(StudentModel,on_delete=models.CASCADE,null=True,verbose_name="Student")
    is_pro = models.BooleanField(default=False)
    paid_date=models.DateField(auto_now_add=True,null=True)
    pro_expiry_date = models.DateField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100 , choices=SUBSCRIPTION , default='FREE')     
        
    def __str__(self):
        return self.subStudent.student_name



