from django import forms
from django.core.mail import message, send_mail
from django.forms.models import ModelForm

from .models import  WhatWeAreDoingDetail


class WhatWeAreDoingDetailForm(forms.ModelForm):
    class Meta:
        model = WhatWeAreDoingDetail
        fields = '__all__'
        exclude = ('id',)


# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'

# class FormEmailContact(forms.ModelForm):
#     fromemail = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(required=True)