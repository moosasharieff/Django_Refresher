"""
URL configuration for test_project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from level_one import views as app1_views
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', app1_views.index, name="main-view")
    # Use 'include' to import all the URLs in the Django App
    path("project_prefix/", include('level_one.urls')),
    path("level_two/", include('level_two.urls')),
    path("level_three/", include('level_three.urls')),
    path("level_four/", include('level_four.urls')),
    path('level_five/', include('level_five.urls'))

]