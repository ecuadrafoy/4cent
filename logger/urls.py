from django.urls import path
from django.conf.urls import url
from . import views
from logger.views import TrafficListView, TagView

app_name = 'logger'

urlpatterns = [
    path('submit/', views.add_traffic, name='add_traffic'),
    path('', views.trafficIndex, name = 'tagged_traffic'),
    path('tag/<slug:tag_slug>/', views.TagView, name = 'tagged_traffic'),
    path('traffic/', TrafficListView.as_view(), name='log_sheet'),
    path('detail/<slug:traffic_post>', views.traffic_detail, name='traffic_detail'),
    ]