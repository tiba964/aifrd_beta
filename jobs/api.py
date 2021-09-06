# views

from .models import WhatWeAreDoingDetail
from .serializers import WhatWeAreDoingDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def what_do_api(request):
    all_whatDoDetail = WhatWeAreDoingDetail.objects.all()
    data = WhatWeAreDoingDetailSerializer(all_whatDoDetail, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def what_do_detail_api(request, id):
    story_detail_detail = WhatWeAreDoingDetail.objects.get(id=id)
    data = WhatWeAreDoingDetailSerializer(what_do_detail).data
    return Response({'data': data})


class WhatWeAreDoingDetailListApi(generics.ListAPIView):
    queryset = WhatWeAreDoingDetail.objects.all()
    serializer_class = WhatWeAreDoingDetailSerializer


class WhatWeAreDoingDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WhatWeAreDoingDetailSerializer
    queryset = WhatWeAreDoingDetail.objects.all()
    lookup_field = 'id'
