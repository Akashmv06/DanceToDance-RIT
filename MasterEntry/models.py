from django.db import models

# Create your models here.

from django_countries.fields import CountryField

class Country(models.Model):
    country=CountryField(null=False)
    
class SubscriptionType(models.Model):
    Subtype=models.CharField("Subscription type",max_length=20,null=False) 
    def __str__(self):
        return(self.Subtype)

class DanceCategory(models.Model):
    dancecategory_name=models.CharField("Dance Category",max_length=20,null=False,unique=True)
    dancecategory_photo=models.FileField("Thumbnail",upload_to="Categ_img",null=True)
    def __str__(self):
        return self.dancecategory_name

class ComplaintType(models.Model):
    complainttype_name=models.CharField("Complaint Type",max_length=20,null=False,unique=True)

    def __str__(self):
        return self.complainttype_name

class Designation(models.Model):
    designation_name=models.CharField("Designation",max_length=20,null=False,unique=True)

    def __str__(self):
        return self.designation_name

class DanceLevel(models.Model):
    dancelevel_name=models.CharField("Dance Level",max_length=20,null=False,unique=True)
    def __str__(self):
        return self.dancelevel_name
    
class NewsType(models.Model):
    newstype_name=models.CharField("News Type",max_length=20,null=False,unique=True)

    def __str__(self):
        return self.newstype_name

class District(models.Model):
    district_name=models.CharField("District",max_length=20,null=False,unique=True)
    def __str__(self):
        return self.district_name

class Place(models.Model):
    place_district=models.ForeignKey(District,on_delete=models.CASCADE,null=True,verbose_name="District")
    place_name=models.CharField("Place",max_length=20,null=False,unique=True)

    def __str__(self):
        return f"({self.place_district})-{self.place_name}"

        class Meta:
            ordering=[1]


