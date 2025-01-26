from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_name=models.CharField(max_length=200)
    profile_image=models.ImageField(upload_to='images')
    
