from .models import TODO
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title','description','date']
        