from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import profile

# Index View
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username = request.user.username)
    user_profile = profile.objects.get(user=user_object)
    return render(request, 'main/index.html',{'user_profile':user_profile})

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

#upload
@login_required(login_url='signin')
def upload(reqeust):
    return HttpResponse('<h1>upload</h1>')

#settings
def settings(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('signin')

    try:
        # Get the user's profile
        user_profile = profile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Handle the case where the profile does not exist
        user_profile = profile.objects.create(user=request.user)

    if request.method == "POST":
        # Get form data
        bio = request.POST.get('bio', '').strip()
        location = request.POST.get('location', '').strip()
        pfp = request.FILES.get('pfp')  # Match the form field name 'pfp'

        # Update profile fields
        if pfp:
            user_profile.profile_img = pfp
        user_profile.bio = bio
        user_profile.location = location

        # Save the profile
        user_profile.save()

        # Redirect to the settings page after saving
        return redirect('settings')

    # Render the settings page with the user's profile data
    return render(request, 'main/setting.html', {'user_profile': user_profile})