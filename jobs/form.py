from django import forms

from .models import WhatWeAreDoingDetail


class WhatWeAreDoingDetailForm(forms.ModelForm):
    class Meta:
        model = WhatWeAreDoingDetail
        fields = '__all__'
        exclude = ('id',)
