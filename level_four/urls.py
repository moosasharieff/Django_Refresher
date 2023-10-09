

from django.urls import path
from level_four import views

# Need to register application name in a variable
# for Django to find the relative URLs paths
app_name = "app_four_application"

urlpatterns = [
    # using different methods to connect with views.func()
    path('', views.app_four, name="app_four_main"),
    path('relative-path', views.relative_url_template, name="relative")
]