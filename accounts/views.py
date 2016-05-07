from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponseRedirect


# Create your views here.

def login(request):
    return render(request, 'login.html', {})


def signup(request):
    form = SignUpForm(request.POST or None)
    return render(request, 'signup.html', {"form":form})

def new_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print request.POST
        if form.is_valid():
            # process the data in form.cleaned_data as required
            firstname = form.cleaned_data.get("name")

            return render(request, 'thanks.html', {"name":firstname})
        else:
            return render(request,'thanks.html',{"name":"data enterd is not valid"})

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {"form": form})

def home(request):
    return render(request, 'home.html', {})

def thanks(request):
    return render(request, 'thanks.html', {"name":"tom"})

