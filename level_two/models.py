from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)

    # print string representation
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)
    url = models.CharField(max_length=256, unique=True)

    # Prints string representation
    def __str__(self):
        return self.name

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()



