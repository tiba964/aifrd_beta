# views

from .models import StoryDetail
from .serializers import StoryDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def stories_api(request):
    all_stories = StoryDetail.objects.all()
    data = StoryDetailSerializer(all_stories, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def story_detail_api(request, id):
    story_detail_detail = StoryDetail.objects.get(id=id)
    data = StoryDetailSerializer(career_detail).data
    return Response({'data': data})


class StoryDetailListApi(generics.ListAPIView):
    queryset = StoryDetail.objects.all()
    serializer_class = StoryDetailSerializer


class StoryDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoryDetailSerializer
    queryset = StoryDetail.objects.all()
    lookup_field = 'id'
