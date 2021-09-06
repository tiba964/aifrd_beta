from django import forms

from .models import CareerDetail


class CareerDetailForm(forms.ModelForm):
    class Meta:
        model = CareerDetail
        fields = '__all__'
        exclude = ('id',)
