from django.db import models

# Create your models here.

class Careers(models.Model):
    candidate_name = models.CharField(max_length=30)
    candidate_mail = models.EmailField()    
    candidate_phone = models.CharField(max_length=15)
    candidate_quali = models.CharField(max_length=40)
    candidate_post = models.CharField(max_length=30)
    condidate_address = models.CharField(max_length=50)
    condidate_cv = models.FileField()
    condidate_message = models.TextField()