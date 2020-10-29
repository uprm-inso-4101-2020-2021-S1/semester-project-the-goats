import datetime

from django import forms
from .models import *


class EventForm(forms.ModelForm):
    day = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)
    start = forms.TimeInput(attrs={'type': 'time'})
    class Meta:
        model = Event

        fields = ['title', 'day', 'start', 'end', 'description']