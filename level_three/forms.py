
from django import forms
from level_three.models import User

class NewUserForm(forms.ModelForm):
    # Custom validators will go here for the forms
    class Meta():
        model = User
        fields = "__all__" # includes all the fields from the model
        # exclude = ["last_name"] # excludes mentioned fields from the model
        # fields = ("email") # includes only mentioned fields from the model
