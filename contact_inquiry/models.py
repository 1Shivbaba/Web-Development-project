from django.db import models

# Create your models here.

class Contact_Inquiry(models.Model):
    contact_name = models.CharField( max_length=30)
    contact_mail = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    contact_subject = models.CharField(max_length=30)
    contact_message = models.TextField()