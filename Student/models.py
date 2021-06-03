from django.db import models
from django.db.models.fields import SlugField
from Accounts.models import StudentModel
from Tutor.models import CourseVideo
from django.utils.text import slugify

# Create your models here.
class Favourites(models.Model):
    fstudent=models.CharField(max_length=40,verbose_name="Student",null=True)
    fvideo=models.ForeignKey(CourseVideo,on_delete=models.SET_NULL,null=True,verbose_name="Video:")
    fdate=models.DateTimeField("Date & Time:",auto_now_add=True)
    slug=models.SlugField(blank=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.fvideo.cv_course)
        super(Favourites,self).save(*args,**kwargs)
    def __str__(self):
        return self.fvideo.cv_title
        