from django.shortcuts import render,redirect
from .models import Profile

# Create your views here.

def profile(request):
    if request.method =="POST" and request.FILES:
        name=request.POST["profile_name"] #frontend bata aako
        image=request.FILES["profile_image"] #frontend bata aako
        rate=request.POST["per_hourrate"]  #frontend bata aako
        user=Profile(profile_name=name,profile_image=image,per_hourrate=rate) #model=frontend part
        user.save()
        return redirect('profile')
    users=Profile.objects.all()
    return render(request,'profile.html',{'users':users})
