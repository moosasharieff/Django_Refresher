from django.db import models

# Importing db models from user authorization section
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    """ Extending 'user' model class with new attributes """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    # Adding attributes (Making this optional for user to add)
    profile_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics') # inside dir: 'media'


    def __str__(self):
        """ :return: username from 'User' Model """
        return self.user.username