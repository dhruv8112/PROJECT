from django.db import models

# Create your models here.
class contact(models.Model):
    
    name=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    Email=models.CharField(max_length=20)
    subject=models.CharField(max_length=25)
    message=models.TextField(max_length=200)