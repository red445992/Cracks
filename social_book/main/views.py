from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User, auth

from .models import profile
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['Email']
        password = request.POST['Password']
        Cpassword = request.POST['Cpassword']

        if password == Cpassword:
            if User.objects.filter(email = email).exists():
                messages.info(request,"email already taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = profile.objects.create(user=user_model,id_user = user_model.id)
                new_profile.save()



                return redirect('signin')
            

        else:
            messages.info(request,'password doesnt match')
            return redirect('signup')

    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')