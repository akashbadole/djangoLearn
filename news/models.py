from turtle import title
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=250)
    news_desc  = HTMLField()