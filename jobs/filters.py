import django_filters
from .models import WhatWeAreDoingDetail


class WhatWeAreDoingDetailFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = WhatWeAreDoingDetail
        fields = '__all__'
        exclude = [
            'id',
            'whatDoDetail_image_gallery',
            'whatDoDetail_image1',
            'whatDoDetail_image2',
            'whatDoDetail_image3',
        ]
