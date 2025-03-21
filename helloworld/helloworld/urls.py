"""
URL configuration for helloworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path

from helloworld.views import main, lunch_list, introduce, sports, music, animal, weather, burger_list, cafe_list, \
    burger_search, cafe_search

urlpatterns = [
       path('admin/', admin.site.urls),
    path("", main),
    path("lunch_list/", lunch_list),
    path("introduce/", introduce),
    path("spo/", sports),
    path("muse/", music),
    path("ani/", animal),
    path("wea/", weather),
    path("list/", burger_list),
    path("cafe/", cafe_list),
    path("search/", burger_search),
    path("cafe_search/", cafe_search)
]
