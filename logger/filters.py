import django_filters
from django import forms
from .models import Traffic

class TrafficFilter(django_filters.FilterSet):
    fulltext = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Traffic
        fields = {'PIR', 'status', 'fulltext','user'}
        help_texts={
            'fulltext': None,
            'PIR': None,
            'status': None,
            'user': None,
        }
        labels = {
            'PIR': ('Filter by PIR'),
            'status': ('Filter by status'),
            'fulltext': ('Filter from traffic text'),
            'tags' : ('Filter by tags'),
        }
        widgets = {
            'PIR': forms.TextInput(attrs={'placeholder': 'Filter by PIR'}),
        }
    