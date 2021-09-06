# views

from .models import CareerDetail
from .serializers import CareerDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def career_list_api(request):
    all_jobs = CareerDetail.objects.all()
    data = CareerDetailSerializer(all_careers, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def career_detail_api(request, id):
    career_detail_detail = CareerDetail.objects.get(id=id)
    data = CareerDetailSerializer(career_detail).data
    return Response({'data': data})


class CareerDetailListApi(generics.ListAPIView):
    queryset = CareerDetail.objects.all()
    serializer_class = CareerDetailSerializer


class CareerDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CareerDetailSerializer
    queryset = CareerDetail.objects.all()
    lookup_field = 'id'
