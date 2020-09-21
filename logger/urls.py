from django.urls import path
from . import views
app_name = 'logger'

urlpatterns = [
    path('', views.traffic_list, name='traffic_list'),
    path('<slug:traffic_post>/', views.traffic_detail, name='traffic_detail')
    ]