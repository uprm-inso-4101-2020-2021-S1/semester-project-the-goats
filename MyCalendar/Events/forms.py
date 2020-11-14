import datetime

from django import forms
from .models import *


class EventForm(forms.ModelForm):
    day = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)
    start = forms.TimeInput(attrs={'type': 'time'})
    rank_choices = [('Friend', 'Friend'), ('Family', 'Family'), ('Acquaintance', 'Acquaintance')]
    rank = forms.ChoiceField(choices=rank_choices, widget=forms.Select())
    class Meta:
        model = Event
        fields = ['title', 'day', 'start', 'end', 'rank', 'description']