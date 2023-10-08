from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Importing model(s)
from level_three.forms import NewUserForm

# Creating new form
def user(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "form.html", context={"form" : form})

    # render the data when user visit the page
    return render(request, "form.html", context={"form" : form})