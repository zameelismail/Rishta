from django.shortcuts import render, redirect
from matrimony_app.forms import contact_form,reg_form, profile_form, user_profile_form
from django.contrib.auth import login, logout, authenticate
from matrimony_app.models import Profile, Interest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        data=contact_form(request.POST)
        if data.is_valid():
            data.save()
    form=contact_form()
    return render(request, 'home.html', {'form':form})

def update_profile(request):
    data=profile_form(request.POST or None, request.FILES or None, instance=request.user.profile)
    data2=user_profile_form(request.POST or None, instance=request.user)
    if data.is_valid() and data2.is_valid():
        data.save()
        data2.save()
        return redirect('/')
    
    return render(request, 'update_profile.html',{'form':data, 'form2':data2})


def my_profile(request):
    if request.user.is_authenticated:
        data=Profile.objects.get(user=request.user)
        return render(request, 'my_profile.html',{'form':data})
    else:
        messages.success(request, "You must be logged in to see your profile!")
        return redirect('/')
        
def view_profile(request, ID):
    data=Profile.objects.get(pk=ID)
    user=request.user.profile
    if request.method == "POST":
        inte = request.POST['follow']
        
        if inte == "unfollow":
            user.follow.remove(data)
            user.save()
        elif inte == "follow":
            user.follow.add(data)
            user.save()
            
    return render(request, 'view_profile.html',{'form':data})

def regs(request):
    form=reg_form()
    if request.method == "POST":
        data=reg_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/logins')
        else:
            messages.success(request, "Pleace Enter Valid Credentials!")
    return render(request, 'regs.html', {'form':form})

def logins(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.success(request, "Pleace Enter Valid Credentials!")
    return render(request, 'logins.html')

def logouts(request):
    logout(request)
    return redirect('/logins')
  
def all_profiles(request):
    if request.user.is_authenticated:
        data=Profile.objects.exclude(user = request.user)
        
        if request.method == "POST":
            ID = request.POST.get["ids"]
            form = Profile.objects.get(pk=ID)
        
        
        
        return render(request, 'all_profiles.html',{'forms':data})
    else:
        messages.success(request, "You must be logged in to see all profile!")
        return redirect('/')
