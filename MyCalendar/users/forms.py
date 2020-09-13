from django import forms
from .models import *
from django.contrib.auth.models import User

class FriendForm(forms.ModelForm):
    rank_choices = [('Friend', 'Friend'), ('Family', 'Family'), ('Acquaintance', 'Acquaintance')]
    rank = forms.ChoiceField(choices=rank_choices, widget=forms.Select())
    class Meta:
        model = Connection
        fields = ['rank','following']

