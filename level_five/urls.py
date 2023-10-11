

from django.urls import path
from level_five import views

# Relative URL Paths
app_name = "level_five_app"

urlpatterns =[
    path('', views.index, name='index'),
    path('register/', views.register, name='registration')
]