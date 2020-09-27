"""collator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from logger.views import TrafficListView, add_traffic, EventCreatePop, get_cat_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logger/', include('logger.urls', namespace='logger')),
    # path('traffic/', TrafficListView.as_view(), name='log_sheet'),
    # path('submit/', add_traffic, name='add_traffic'), # For some reason if I erase this path, the one from logger/urls.py won't work
    url(r'create_cat/', EventCreatePop, name = 'CategoryCreate'),
    url(r'^category/ajax/get_cat_id', get_cat_id, name = "get_cat_id"),

]
