import django_filters
from .models import StoryDetail


class StoryDetailFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StoryDetail
        fields = '__all__'
        exclude = ['story_image_one',
                   'story_image_two',
                   'story_image_three',
                   'id'
                   ]
