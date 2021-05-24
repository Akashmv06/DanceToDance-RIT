from MasterEntry.models import DanceCategory, Designation,District
from django.db import models
from django.db.models.base import Model

class CoursePlaylist(models.Model):
    #course_dancecategory=models.ForeignKey(DanceCategory,on_delete=models.SET_NULL,null=True,verbose_name="Dance Category:")
   
    course_title=models.CharField("Title",max_length=50,null=False)

    def __str__(self):
            return(self.course_title)
        

class CourseVideo(models.Model):

    cv_playid=models.ForeignKey(CoursePlaylist,on_delete=models.SET_NULL,null=True,verbose_name="Dance Category:")
    cv_title=models.CharField("Title",max_length=50,null=False)
    cv_video=models.FileField("Video",upload_to="video")
    
    def __str__(self):
            return f"{self.cv_playlist}-{self.cv_title}"


   
    



