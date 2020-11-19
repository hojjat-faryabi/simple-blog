from django import forms
from . import models

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = ['name', 'message']
        labels = {'name':"", 'message':""}
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder':'name'
            }),

            'message' : forms.Textarea(attrs={
                'rows':'8',
                'cols':'80',
                'placeholder':'message',
            })
        }