from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from .forms import SignUpForm, LoginForm


# Create your views here.

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        print  request.POST
        print timezone.now()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    auth_login(request, user)
                    return render(request, 'info.html', {"data": "User is valid, active, authenticated and Logined"})
                else:
                    print("The password is valid, but the account has been disabled!")
                    return render(request, 'info.html', {"data": "The password is valid, but the account has been disabled!"})
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
                return render(request, 'info.html', {"data": "The username and password were incorrect.!"})
        else:
            return render(request, 'info.html', {"data": " Invalid information submitted"})
    return render(request, 'login.html', {"form": form})


def signup(request):
    form = SignUpForm(request.POST or None)
    return render(request, 'signup.html', {"form": form})


def new_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print request.POST
        print timezone.now()
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            gender = form.cleaned_data.get("gender")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            about = form.cleaned_data.get("about")
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.date_joined = timezone.now()
            user.save()

            return render(request, 'info.html', {"data": first_name +" Thanks for new registration" })
        else:
            return render(request, 'info.html', {"data": "Data enterd is not valid, Thanks"})

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {"form": form})


def home(request):
    return render(request, 'home.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'info.html', {"data": "Logout sucessfully"})

def verify(request):
    if request.method=='GET':
        print request.GET
    return render(request, 'info.html', {"data":"This page is to check the GET Method"})



