from django import forms
from .models import Responses
from django.db import models


class Messages(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ('message', 'name','email', 'subject' )