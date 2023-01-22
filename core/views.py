from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {})

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
                return redirect('index')
        else:
            messages.info(request, 'Password not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {})
