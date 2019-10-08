from django.shortcuts import render,redirect
from .forms import UserForm, UserProfileInfoForm

# Imports for user Login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

# Use decorator to require a user to be logged in to see this view
@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))

def register(request):
    # assume they aren't registered
    registered = False

    if request.method == 'POST':
        # Grab information off the forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see if forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
        # Check to see if there is a picture
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            # If form is invalid
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request,'registration.html',context)

def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('myapp:index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,'login.html',{})
