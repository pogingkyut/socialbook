from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'index.html', {'user_profile': user_profile})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()

                return redirect('settings')
        else:
            messages.info(request, 'Password not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {})

def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Wrong username and/or password!')
        
    return render (request, 'signin.html', {})

@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def settings(request):

    user_profile=Profile.objects.get(user=request.user)

    # if user_profile.user == None:
    #     return redirect('index')
   
    if request.method=='POST':

        if request.FILES.get('image') == None:
            image=user_profile.profileimg
        else:
            image=request.FILES.get('image')
        
        bio = request.POST['bio']
        location = request.POST['location']

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()

        return redirect('settings')
        
    
    return render (request, 'setting.html', {'user_profile':user_profile})

@login_required(login_url='signin')
def upload(request):
    return render(request, 'index.html', {})