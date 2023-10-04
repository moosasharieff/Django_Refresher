from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Importing db models
from level_two.models import AccessRecords

def index(request):
    # pulling 'AccessRecords' data
    records = AccessRecords.objects.order_by('date')
    data_dict = {"access_records" : records}
    return render(request, "access_records.html", context=data_dict)


