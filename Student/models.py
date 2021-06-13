from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import SlugField
from Accounts.models import StudentModel
from Tutor.models import CourseVideo
from django.utils.text import slugify
from MasterEntry.models import ComplaintType

# Create your models here.
class Favourites(models.Model):
    fstudent=models.CharField(max_length=40,verbose_name="Student",null=True)
    fvideo=models.ForeignKey(CourseVideo,on_delete=models.SET_NULL,null=True,verbose_name="Video:")
    fdate=models.DateTimeField("Date & Time:",auto_now_add=True)
    slug=models.SlugField(blank=True)
    is_fav=models.BooleanField(default=False)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.fvideo.cv_course)
        super(Favourites,self).save(*args,**kwargs)
    def __str__(self):
        return self.fvideo.cv_title

class videofeedback(models.Model):
    vfstudent=models.ForeignKey(StudentModel,on_delete=models.CASCADE,null=True,verbose_name="Student")     
    vfvideo=models.ForeignKey(CourseVideo,on_delete=models.CASCADE,null=True,verbose_name="Video:")
    vcontent=models.TextField(max_length=300,null=True,verbose_name="Content")
    vview=models.BooleanField(verbose_name="Is liked",default=False)
    vfsend=models.DateTimeField(auto_now_add=True,verbose_name="Send date" , null=True)
    def __str__(self):
        return f"{self.vcontent} by {self.vfstudent.student_name}"

        
class Feedback(models.Model):
    feedstudent=models.ForeignKey(StudentModel, verbose_name="Student", on_delete=models.CASCADE,null=True)
    feedtype=models.ForeignKey(ComplaintType,on_delete=models.CASCADE,null=True,verbose_name="Choose feedback type")
    feedsend=models.DateTimeField(auto_now_add=True,verbose_name="Send date",null=True)
    feedcontent=models.TextField(max_length=300,verbose_name="Give feedback",null=True)

    def __str__(self):
        return f"{self.feedcontent} by {self.feedstudent.student_name}"