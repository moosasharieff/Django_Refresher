

from django.urls import path
from level_one import views

urlpatterns = [
    path('app_prefix/', views.index, name='index')
]