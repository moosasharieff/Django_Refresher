from django.shortcuts import render
from level_five.forms import UserForm, UserProfileInfoForm


# Create your views here.

# Create index view
def index(request):
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
