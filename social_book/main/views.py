from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import profile

# Index View
@login_required(login_url='signin')
def index(request):
    return render(request, 'main/index.html')

# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['Email']
        password = request.POST['Password']
        Cpassword = request.POST['Cpassword']

        if password == Cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username,password=password)
                auth.login(request,user_login)

                user_model = User.objects.get(username=username)
                new_profile = profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()

                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('signin')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')

    return render(request, 'main/signup.html')

# Signin View
def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('signin')

    return render(request, 'main/signin.html')

# Logout View
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('signin')

def settings(request):
    user_profile = profile.objects.get(user=request.user)

    return render(request,'main/setting.html',{'user_profile':user_profile})