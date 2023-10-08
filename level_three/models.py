from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"""
            First Name : {self.first_name},
            Last Name  : {self.last_name},
            Email      : {self.email}
        """
