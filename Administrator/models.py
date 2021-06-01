from django.db import models
from django.db.models.fields import TextField
from MasterEntry.models import Designation,DanceCategory,District,NewsType,DanceLevel, SubscriptionType
from django.utils.text import slugify

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
    course_level=models.ForeignKey(DanceLevel,on_delete=models.SET_NULL,verbose_name="Level",null=True)
    course_subs=models.ForeignKey(SubscriptionType,on_delete=models.CASCADE,verbose_name="Subscription type",null=True)
    slug= models.SlugField(blank=True)
    is_premium=models.BooleanField(default=False)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.course_name)
        super(DanceCourses,self).save(*args,**kwargs)
    
    def __str__(self):
        return (self.course_name)

        

class News(models.Model):
    news_title=models.CharField("News title", max_length=50,null=False)
    news_content=models.TextField("News Content")
    news_newstype=models.ForeignKey(NewsType,on_delete=models.SET_NULL,null=True,verbose_name="News Type:")
    news_uploaddate=models.DateField("Upload Date", auto_now_add=True)
    news_poster=models.ImageField( "Poster",upload_to='news')
    news_loc=models.CharField("Location",max_length=50,null=True)
    news_date=models.DateField("Date",null=True)
    
    
    def __str__(self):
        return (self.news_title)



   



