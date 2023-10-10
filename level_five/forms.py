

from django import forms

# Importing built-in User Model and OnetoOne Relationship Model
from django.contrib.auth.models import User
from level_five.models import UserProfileInfo

class UserForm(forms.ModelForm):
    """ Creates ModelForm for built-in User Model and OnetoOne Relationship Model. """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        """ Create a model for only 'username', 'password' and 'email' attribute only. """
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(form.ModelForm):
    """ Creates a ModelForm for extended attributes in the db for 'profile_site' and 'profile_pic'  """
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
