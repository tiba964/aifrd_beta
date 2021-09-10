from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import Application, Slider,  VisionMissionValue, Volunteer, WhatWeAreDoingBackgroundImage, WhoWeAre, Index, Donate, WhatWeAreDoingDetail, About, GetInvolved
from .serializers import ApplicationSerializer, SliderSerializer, VisionMissionValueSerializer, WhoWeAreSerializer, VolunteerSerializer, IndexSerializer, DonateSerializer, WhatWeAreDoingDetailSerializer, AboutSerializer, GetInvolvedSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .filters import WhatWeAreDoingDetailFilter
from django.core.paginator import Paginator

from blogs.models import StoryDetail
from django.core.mail import send_mail

class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ApplicationRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
template_name = "applicantsList.html"


def applicantsList(request):
    """Renders the applicants list page."""
    assert isinstance(request, HttpRequest)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer(queryset, many=True)

    full_name = request.GET.get('full_name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    region = request.GET.get('region')
    address = request.GET.get('address')
    gender = request.GET.get('gender')
    english = request.GET.get('english')
    arabic = request.GET.get('arabic')
    kurdish = request.GET.get('kurdish')
    cover_letter = request.GET.get('cover_letter')
    upload_cv = request.GET.get('upload_cv')

    application = Application.objects.create(full_name=full_name,
                                             email=email,
                                             phone=phone,
                                             region=region,
                                             address=address,
                                             gender=gender,
                                             english=english,
                                             arabic=arabic,
                                             kurdish=kurdish,
                                             cover_letter=cover_letter,
                                             upload_cv=upload_cv,)

    return render(request, 'applicantsList.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def volunteer(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer(queryset, many=True)

    return render(request, 'volunteer.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def index(request):
    assert isinstance(request, HttpRequest)
    queryset = Index.objects.all()
    serializer_class = IndexSerializer(queryset, many=True)

    stories = StoryDetail.objects.all()
    whatWeDo = WhatWeAreDoingDetail.objects.all()

    # Show many contacts per page for stories
    paginator_story = Paginator(stories, 10000000000000000)
    page_number_story = request.GET.get('page')
    page_obj_story = paginator_story.get_page(page_number_story)

    # Show many contacts per page for what we are doing
    paginator = Paginator(whatWeDo, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    slider_show = Slider.objects.all()[:4]
    context = {
        'data': serializer_class.data,
        'slider_show': slider_show,
        'whatWeDoss': page_obj,
        'stories': page_obj_story,
    }
    return render(request, 'index.html', context)


def donate(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer(queryset, many=True)

    return render(request, 'donate.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def contact(request):
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'phone' : phone,
            'email' : email,
            'subject' : subject,
            'message' : message,
        }
        print(data)
        message = ''' 
        New message :{}
        From: {}
        '''.format(data['message'], data['email'])

        if subject and message and email:
            try:
                send_mail(data['subject'], message, from_email= 'contact@aifrd.org',recipient_list= ['contact@aifrd.org'],  fail_silently=False)

            except  Exception as error:
                return HttpResponse('Invalid header found.')
    return render(request, 'contact.html')

def volunteerForm(request):
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
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
        New Volunteer :{}
        From: {}
        Phone: {}
        Region: {}
        Gender: {}
        Address:{}
        CV: {}
        Language:{}
        Cover_letter: {}


        '''.format(data['name'], data['email'], data['phone'], data['region'], data['gender'], data['address'], data['upload_cv'], data['select_language'], data['cover_letter'])

        if name and gender and email and phone and  region and address and   upload_cv and select_language and cover_letter:
            try:
                send_mail(data['name'], message, from_email= 'volunteer@aifrd.org',recipient_list= ['volunteer@aifrd.org'],  fail_silently=False)

            except  Exception as error:
                return HttpResponse('Invalid header found.')
    return render(request, 'volunteer.html')


def what_we_are_doing(request):
    """Renders the create what_we_are_doing page."""
    whatWeDo = WhatWeAreDoingDetail.objects.all()

    # filters
    myfilter = WhatWeAreDoingDetailFilter(request.GET, queryset=whatWeDo)
    whatWeDo = myfilter.qs
    bg_image_what_we_are_doing = WhatWeAreDoingBackgroundImage.objects.all()
     
    # Show many contacts per page.
    paginator = Paginator(whatWeDo, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if whatWeDo:
        context = {'whatWeDoss': page_obj,
                   'myfilter': myfilter,
                   'bg_image_what_we_are_doing':bg_image_what_we_are_doing}  # template name

    else:
        context = {'message': "There are no WhatWeDo available at the moment."}
    return render(request, 'what_we_are_doing.html', context)


def what_we_are_doing_details(request, id):
    """Renders the create what_we_are_doing_details page."""
    whatWeDo = WhatWeAreDoingDetail.objects.get(id=id)

    context = {'whatWeDo': whatWeDo}
    return render(request, 'what_we_are_doing_details.html', context)


def vision_mission_value(request):
    """Renders the create VisionMissionValue page."""
    assert isinstance(request, HttpRequest)
    queryset = VisionMissionValue.objects.all()
    serializer_class = VisionMissionValueSerializer(queryset, many=True)

    return render(request, 'vision_mission_value.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def about(request):
    """Renders the create about page."""
    assert isinstance(request, HttpRequest)
    queryset = About.objects.all()
    serializer_class = AboutSerializer(queryset, many=True)

    return render(request, 'about.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def get_involved(request):
    """Renders the create get_involved page."""
    assert isinstance(request, HttpRequest)
    queryset = GetInvolved.objects.all()
    serializer_class = GetInvolvedSerializer(queryset, many=True)

    return render(request, 'get_involved.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def who_we_are(request):
    """Renders the create who_we_are page."""
    assert isinstance(request, HttpRequest)
    queryset = WhoWeAre.objects.all()
    serializer_class = WhoWeAreSerializer(queryset, many=True)

    return render(request, 'who_we_are.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
