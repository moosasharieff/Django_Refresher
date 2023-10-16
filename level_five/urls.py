

from django.urls import path
from level_five import views

# Relative URL Paths
app_name = "level_five_app"

urlpatterns =[
    path('', views.level_index, name='level_index'),
    path('register/', views.register, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('special/', views.special, name='special'),
]