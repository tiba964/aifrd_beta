from django import forms

from .models import StoryDetail


class StoryDetailForm(forms.ModelForm):
    class Meta:
        model = StoryDetail
        fields = '__all__'
        exclude = ('id',)
