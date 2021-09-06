from django.shortcuts import redirect, render
from .models import CareerDetail, CareerList, CareerDetatilImage
from django.core.paginator import Paginator
from .form import CareerDetailForm
from django.urls import reverse
from django.http import HttpRequest
from .serializers import CareerDetailSerializer, CareerListSerializer, CareerDetatilImageSerializer
from .filters import CareerDetailFilter

# Create your views here.


def career_list(request):
    career_list = CareerDetail.objects.all()
    assert isinstance(request, HttpRequest)
    queryset = CareerList.objects.all()
    serializer_class = CareerListSerializer(queryset, many=True)

    # filters
    myfilter = CareerDetailFilter(request.GET, queryset=career_list)
    career_list = myfilter.qs

    # Show many contacts per page.
    paginator = Paginator(career_list, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if career_list:
        context = {'careers': page_obj, 'myfilter': myfilter,
                   'data': serializer_class.data}  # template name

    else:
        context = {'message': "There are no jobs available at the moment."}
    return render(request, 'career_list.html', context)


def career_detail(request, id):
    career_detail = CareerDetail.objects.get(id=id)

    assert isinstance(request, HttpRequest)
    queryset = CareerDetatilImage.objects.all()
    serializer_class = CareerDetatilImageSerializer(queryset, many=True)

    context = {'career': career_detail, 'data': serializer_class.data}
    return render(request, 'career_detail.html', context)
