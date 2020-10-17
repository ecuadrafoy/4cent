from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from django import forms
from django.utils import timezone
from django_tables2 import SingleTableView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from taggit.models import Tag

from .models import Traffic, event_type, Notes
from .tables import TrafficTable
from .forms import TrafficForm, CategoryForm, NoteForm

@login_required()
def trafficIndex(request):
    traffics = Traffic.objects.all()
    common_tags = Traffic.tags.most_common()[:4]
    context = {'traffics':traffics,
               'common_tags':common_tags,}
    return render(request, 
                  'logger/traffic/list.html', 
                  context)

def TagView(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    common_tags = Traffic.tags.most_common()[:4]
    traffics = Traffic.objects.filter(tags=tag)
    context = {'tag':tag,
               'common_tags':common_tags,
               'traffics':traffics}
    return render(request, 
                  'logger/traffic/list.html',
                   context)
    
@login_required()
def traffic_detail(request, traffic_post):
    traffic_post = get_object_or_404(Traffic,
                                     traffic_slug = traffic_post)
    #adding the comment section after this
    notes = traffic_post.notes.filter(active = True)
    new_note = None
    if request.method == 'POST':
        note_form = NoteForm(data=request.POST)
        if note_form.is_valid():
            new_note = note_form.save(commit=False)
            new_note.user = request.user
            new_note.traffic = traffic_post
            new_note.save()
            note_form = NoteForm()
            messages.success(request, 'Note added successfully')
        else:
            messages.error(request, 'Failed submission, please verify')
            return render(request,
                'logger/traffic/detail.html', 
                {'traffic_post':traffic_post,
                 'notes':notes,
                 'new_note':new_note,
                 'note_form':note_form})
    else:
        note_form = NoteForm()
    return render(request,
                'logger/traffic/detail.html', 
                {'traffic_post':traffic_post,
                 'notes':notes,
                 'new_note':new_note,
                 'note_form':note_form})


class TrafficListView(SingleTableView):
    model = Traffic
    table_class = TrafficTable
    template_name = 'logger/traffic.html'
  
@login_required()
def add_traffic(request):
    if request.method == 'POST':
        form = TrafficForm(request.POST)
        if form.is_valid():
            traffic = form.save(commit=False)
            traffic.user = request.user
            traffic.save()
            form.save_m2m()
            form = TrafficForm()
            messages.success(request, 'Submission Successful')
        else:
            messages.error(request, 'Failed submission, please verify')
            return render(request, 'logger/submit.html',
                          {'form':form})
    # If the form is invalid, show empty form
    else:
        form = TrafficForm()
    return render(request, 'logger/submit.html', 
                  {'form': form})
    


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


