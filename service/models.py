from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_number = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_desc = models.TextField()


# class AboutUs(models.Model):
#     AboutUs_img = models.CharField(max_length=50) #need to add from file
#     AboutUs_small_title = models.CharField(max_length=50)
#     AboutUs_title = models.CharField(max_length=50)
#     AboutUs_desc = models.CharField(max_length=50)
