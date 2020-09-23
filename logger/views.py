from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from django import forms
from django.utils import timezone
from django_tables2 import SingleTableView
from django.views.decorators.csrf import csrf_exempt

from .models import Traffic, event_type
from .tables import TrafficTable
from .forms import TrafficForm, CategoryForm

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

class TrafficListView(SingleTableView):
    model = Traffic
    table_class = TrafficTable
    template_name = 'logger/traffic.html'

def add_traffic(request):
    if request.method == 'POST':
        form = TrafficForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('add_traffic'))
            except:
                pass
        else:
            return render(request, 'logger/submit.html',
                        {'form':form})
    # If the form is invalid, show empty form
    else:
        form = TrafficForm()
    return render(request, 'logger/submit.html', {'form': form})

def EventCreatePop(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_event_type");</script>' % (instance.pk, instance))
    
    return render(request, 'logger/category_form.html',
                    {'form' : form})

@csrf_exempt
def get_cat_id(request):
    if request.is_ajax():
        event_name = request.GET['event_name']
        event_id = event_type.objects.get(name = event_name).id
        data = {'event_id' : event_id}
        return HttpResponse(json.dumps(data), content_type = 'application/json')
    return HttpResponse('/')

