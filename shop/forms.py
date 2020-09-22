from django import forms
from .models import Contact
from django.forms import ModelForm

class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=200)
    email = forms.EmailField(label='Email Address', max_length=200)
    message = forms.CharField(widget=forms.Textarea, label='Message')
    class Meta:
        model= Contact
        fields = ['subject', 'email', 'message']


