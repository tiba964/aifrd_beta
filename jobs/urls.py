from django.urls import path
from . import views
from django.contrib import admin
from . import views
from . import api

app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'),
    path('applicantsList/', views.applicantsList, name='applicantsList'),
    path('volunteer/', views.volunteerForm, name='volunteer'),
    
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('vision_mission_value/', views.vision_mission_value,
         name='vision_mission_value'),
    path('about/', views.about, name='about'),
    path('who_we_are/', views.who_we_are, name='who_we_are'),
    path('get_involved/', views.get_involved, name='get_involved'),
    path('get_involved/', views.get_involved, name='get_involved'),
    path('what_we_are_doing/', views.what_we_are_doing, name='what_we_are_doing'),
    path('what_we_are_doing_details/<int:id>', views.what_we_are_doing_details,
         name='what_we_are_doing_details'),

    # api
    path('api/what_do', api.what_do_api, name='what_do_api'),
    path('api/what_do_detail/<int:id>',
         api.what_do_detail_api, name='what_do_detail_api'),

    # class based views
    path('api/v2/what_do', api.WhatWeAreDoingDetailListApi.as_view(),
         name='WhatWeAreDoingDetailListApi'),
    path('api/v2/what_do_detail/<int:id>',
         api.WhatWeAreDoingDetailDetail.as_view(), name='WhatWeAreDoingDetailDetail'),

]
