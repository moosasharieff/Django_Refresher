from django.contrib import admin

# Register your models here.

# importing Django appliation models
from level_two.models import Topic, Webpage, AccessRecords

# Registering models with Admin
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecords)