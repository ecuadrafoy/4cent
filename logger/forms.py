from django.forms import ModelForm, Textarea, TextInput, DateTimeInput, HiddenInput
from bootstrap_datepicker_plus import DateTimePickerInput
from .models import Traffic, event_type, Notes
import re

class TrafficForm(ModelForm):
    class Meta:
        model = Traffic
        fields = ('docname', 'docdate','category','grids', 'source', 'PIR', 'status','fulltext','tags')
        help_texts={
            'docname': None,
            'grids': None,
            'fulltext': None
        }
        labels = {
            'docname': ('Title of the Document'),
            'docdate': ('Date of the Document'),
            'grids': ('Coordinates'),
            'fulltext': ('Content'),
            'tags': ('Tags'),

        }
        widgets = {
            'docname': TextInput(attrs={'placeholder': 'Enter title of document'}),
            'grids': TextInput(attrs={'placeholder': 'Write coordinates (MGRS)'}),
            'docdate': DateTimePickerInput(),
            'fulltext': Textarea(attrs={'placeholder': 'Enter the full traffic text if possible'}),
            'tags': TextInput(attrs={'data-role': 'tagsinput'})
         
        }
class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ('title','body')
        

class CategoryForm(ModelForm):
    class Meta:
        model = event_type
        fields = [
            'event_type'
            ]