from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Traffic

def traffic_list(request):
    traffics = Traffic.objects.all()
    return render(request,
                'logger/traffic/list.html',
                {'traffics':traffics})

def traffic_detail(request, traffic_post):
    traffic_post = get_object_or_404(Traffic, 
                                traffic_slug=traffic_post, 
                                )
    return render(request,'logger/traffic/detail.html', 
                {'traffic_post':traffic_post})



