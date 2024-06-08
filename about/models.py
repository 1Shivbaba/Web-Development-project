from django.db import models
from tinymce.models import HTMLField

# Create your models 

class About(models.Model):
    about_title = models.CharField(max_length=50)    
    about_desc = HTMLField()
    about_img = models.FileField(upload_to="about/", max_length=250, null=True,default=None)
