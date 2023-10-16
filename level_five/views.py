from django.shortcuts import render, redirect
from level_five.forms import UserForm, UserProfileInfoForm

# Imports for creating Login view
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

# Create index view
def level_index(request):
    """ This is the initial page for the user to view Django Framework of level 5. """
    return render(request, 'level_five_index.html')


# Create registration view
def register(request):
    """ This view will be the landing page for the user when registering. This view will
        also process the data received from user post registering to website """

    registered = False  # Changing view in register.html based on boolean condition

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            # Saving the data
            user = user_form.save()
            user.set_password(user.password)  # hashing the password with Argon2 Hasher and saving it.
            user.save()

            # Validating if user uploaded any data in user_profile_form
            profile = user_profile_form.save(commit=False)  # Not saving the data
            profile.user = user  # Connecting OneToOne relationship with 'user' ModelForm

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, user_profile_form.errors)
    else:
        user_form = UserForm()
        user_profile_form = UserProfileInfoForm()

    return render(request, 'registration.html',
                  {'registered': registered,
                   'user_form': user_form,
                   'user_profile_form': user_profile_form})

# Create Login view
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # We're redirected to a page when func : 'index' lands
                # return HttpResponseRedirect(reverse('level_index'))
                # return redirect(level_index(request))
                return render(request, 'level_five_index.html')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and Password: {password} was used")
            return HttpResponse("invalid login details were provided!")
    else:
        return render(request, "login.html")


def user_logout(request):
    logout(request)
    return render(request, 'level_five_index.html')
    # return redirect(level_index)
    # return HttpResponseRedirect(revese('level_index'))

@login_required
def special(request):
    return HttpResponse("Your are logged in!")