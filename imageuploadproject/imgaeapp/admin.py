from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','profile_name','profile_image','per_hourrate']

admin.site.register(Profile,ProfileAdmin)

