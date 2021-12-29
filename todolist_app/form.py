from django import forms
from django.forms import fields
from todolist_app.models import tasklist

class Taskforms(forms.ModelForm):
        class Meta:
            model = tasklist
            fields = ['task', 'done']