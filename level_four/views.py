from django.shortcuts import render

# Create your views here.
def app_four(request):
    return render(request, "app_four.html")


def relative_url_template(request):
    return render(request, "relative_html_page.html")