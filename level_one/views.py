from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {
        "Grateful" : "Alhamdulillah"
    }

    # return HttpResponse("<em> Assalamualaikum Moosa !")
    return render(request, 'access_records.html', context=my_dict)