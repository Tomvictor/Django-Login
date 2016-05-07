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
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            # redirect to a new URL:

            # return HttpResponseRedirect('/thanks/')

            return render(request, 'thanks.html', {})

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {"form": form})

def home(request):
    return render(request, 'home.html', {})

def thanks(request):
    return render(request, 'thanks.html', {})

