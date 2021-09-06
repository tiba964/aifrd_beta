from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Application, Slider, Contact, VisionMissionValue, Volunteer, WhatWeAreDoingBackgroundImage, WhoWeAre, Index, Donate, WhatWeAreDoingDetail, About, GetInvolved
from .serializers import ApplicationSerializer, SliderSerializer, VisionMissionValueSerializer, ContactSerializer, WhoWeAreSerializer, VolunteerSerializer, IndexSerializer, DonateSerializer, WhatWeAreDoingDetailSerializer, AboutSerializer, GetInvolvedSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .filters import WhatWeAreDoingDetailFilter
from .form import WhatWeAreDoingDetailForm
from django.core.paginator import Paginator
from blogs.filters import StoryDetailFilter
from blogs.form import StoryDetailForm
from blogs.models import StoryDetail


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
    """Renders the create contact page."""
    return render(request, 'contact.html')


def contactList(request):
    """Renders the create contact page."""
    assert isinstance(request, HttpRequest)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer(queryset, many=True)
    full_name = request.GET.get('full_name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    subject = request.GET.get('subject')
    message = request.GET.get('message')
    contactcreated = Contact.objects.create(full_name=full_name,
                                            email=email,
                                            phone=phone,
                                            subject=subject,
                                            message=message,
                                            )
    return render(request, 'contactList.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def what_we_are_doing(request):
    """Renders the create volunteer page."""
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
    """Renders the create volunteer page."""
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
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = About.objects.all()
    serializer_class = AboutSerializer(queryset, many=True)

    return render(request, 'about.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def get_involved(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = GetInvolved.objects.all()
    serializer_class = GetInvolvedSerializer(queryset, many=True)

    return render(request, 'get_involved.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def who_we_are(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = WhoWeAre.objects.all()
    serializer_class = WhoWeAreSerializer(queryset, many=True)

    return render(request, 'who_we_are.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
