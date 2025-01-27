from django.shortcuts import render,redirect
from .models import Profile

# Create your views here.

def profile(request):
    if request.method =="POST" and request.FILES:
        name=request.POST["profile_name"] #frontend bata aako
        print(name)
        image=request.FILES["profile_image"] #frontend bata aako
        print(image)
        user=Profile(profile_name=name,profile_image=image) #model=frontend part
        user.save()
        return redirect('profile')
    return render(request,'profile.html')
