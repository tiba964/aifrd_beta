import django_filters
from .models import CareerDetail


class CareerDetailFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CareerDetail
        fields = '__all__'
        exclude = ['published', 'image_career_details', 'id']
