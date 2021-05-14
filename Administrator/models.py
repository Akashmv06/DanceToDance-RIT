from django.db import models
from MasterEntry.models import Designation,DanceCategory,District

# Create your models here
Gender=(
    ("M","Male"),
    ("F","Female"),
    ("O","Others"),
)

isActive=(
    ("1","Active"),
    ("0","Not Active"),
)


class Tutor(models.Model):
    tutor_name=models.CharField("Name:",max_length=20,null=False)
    tutor_contact=models.CharField("Conatct:",max_length=11,null=False)
    tutor_email=models.EmailField("Email:",unique=True,null=False,help_text="Enter Valid Email")
    tutor_gender=models.CharField("Gender:",max_length=5,choices=Gender,null=False)
    tutor_photo=models.ImageField("Tutor Photo:",upload_to="TutorPhoto",null=False)
    tutor_dob=models.DateField("Date of Birth:",null=False)
    tutor_isactive=models.CharField("Is Active:",max_length=5,choices=isActive,null=False,help_text="If Value is 1 Tutor is Active and Not Active if 0")
    tutor_username=models.CharField("User name:",max_length=15,unique=True,null=False)
    tutor_password=models.CharField("Password:",max_length=15,unique=True,null=False)
    
    tutor_designation=models.ForeignKey(Designation,on_delete=models.SET_NULL,null=True,verbose_name="Designation:")
    tutor_dancecategory=models.ForeignKey(DanceCategory,on_delete=models.SET_NULL,null=True,verbose_name="Dance Category:")
    tutor_district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True,verbose_name="District:")

    def __str__(self):
        return f"{self.tutor_name}-{self.tutor_designation}"
    

class DanceCourses(models.Model):
    course_dancecategory=models.ForeignKey(DanceCategory,on_delete=models.SET_NULL,null=True,verbose_name="Dance Category:")
    course_tutor=models.ForeignKey(Tutor,on_delete=models.SET_NULL,null=True,verbose_name="Tutor:")
    
    course_name=models.CharField("Name:",max_length=20,null=False)
    course_photo=models.ImageField(upload_to="CoursePhoto",null=False)
    course_description=models.TextField("Description")
    course_totalfees=models.CharField("Total Fees:",max_length=20,null=False,)
    course_downpayment=models.CharField("Down Payment:",max_length=20,null=False,help_text="Online Registration Amount:")
    course_details=models.FileField("Course Syllabus:",upload_to="CourseSyllabus")
    course_remarks=models.TextField("Remarks")
   



