from email.policy import default
from turtle import title
from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=250)
    news_desc  = HTMLField()
    slug  = AutoSlugField(populate_from='news_title', unique=True, null=True, default=None)

