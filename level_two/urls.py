

from django.urls import path
from level_two import views

urlpatterns = [
    path('', views.index, name='index')
]