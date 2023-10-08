
from django.urls import path
from level_three import views

urlpatterns = [
    path('', views.user, name="form_name")
]