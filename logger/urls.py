from django.urls import path
from django.conf.urls import url
from . import views
from logger.views import TrafficListView

app_name = 'logger'

urlpatterns = [
    path('submit/', views.add_traffic, name='add_traffic'),
    path('detail/', views.traffic_list, name='traffic_list'),
    path('traffic/', TrafficListView.as_view(), name='log_sheet'),
    path('<slug:traffic_post>/', views.traffic_detail, name='traffic_detail'),
    ]