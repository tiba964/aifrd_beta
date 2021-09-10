from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import CareerDetail, CareerList, CareerDetatilImage
from django.core.paginator import Paginator
from .form import CareerDetailForm
from django.urls import reverse
from django.http import HttpRequest
from .serializers import CareerDetailSerializer, CareerListSerializer, CareerDetatilImageSerializer
from .filters import CareerDetailFilter
from django.core.mail import send_mail

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
def careerForm(request):
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
        career_name = request.POST.get('career_name')
        gender = name = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        region = request.POST.get('region')
        address = request.POST.get('address')
        upload_cv = request.POST.get('upload_cv')
        select_language = request.POST.get('select_language')
        cover_letter = request.POST.get('cover_letter')
        data = {
            'name': name,
            'career_name':career_name,
            'gender' : gender,
            'email' : email,
            'phone' : phone,
            'region' : region,

            'address': address,
            'upload_cv' : upload_cv,
            'select_language' : select_language,
            'cover_letter' : cover_letter,
        }
        print(data)
        message = ''' 
        New applicant :{}
        From: {}
        Career Name : {}
        Phone: {}
        Region: {}
        Gender: {}
        Address:{}
        CV: {}
        Language:{}
        Cover_letter: {}


        '''.format(data['name'], data['email'],data['career_name'], data['phone'], data['region'], data['gender'], data['address'], data['upload_cv'], data['select_language'], data['cover_letter'])

        if name and gender and email and career_name and phone and  region and address and   upload_cv and select_language and cover_letter:
            try:
                send_mail(data['career_name'], message, from_email= 'hr@aifrd.org',recipient_list= ['hr@aifrd.org'],  fail_silently=False)

            except  Exception as error:
                return HttpResponse('Invalid header found.')
    return render(request, 'formCareer.html')

