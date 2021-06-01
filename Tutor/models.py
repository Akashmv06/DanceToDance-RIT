from MasterEntry.models import DanceCategory, Designation,District
from django.db import models
from django.db.models.base import Model
from Administrator.models import DanceCourses


        

class CourseVideo(models.Model):

    cv_title=models.CharField("Title",max_length=50,null=False)
    cv_video=models.FileField("Video",upload_to="video")
    cv_thumbnail=models.FileField("Thumbnail",upload_to="thumbnail",null=True)
    cv_course=models.ForeignKey(DanceCourses, on_delete=models.CASCADE,null=True,verbose_name="Course")
    

    
    def __str__(self):
            return f"{self.cv_course}-{self.cv_title}"


   
    



