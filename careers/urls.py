from django.urls import include, path

from . import views
from . import api


app_name = 'careers'

urlpatterns = [
    path('careerlist/', views.career_list, name='career_list'),
    path('careerdetail/<int:id>', views.career_detail, name='career_detail'),

    # api
    path('api/careers', api.career_list_api, name='career_list_api'),
    path('api/careers/<int:id>', api.career_detail_api, name='career_detail_api'),
    path('api/careerForm/<str:carrer_name>', views.careerForm, name='careerForm'),

    # class based views
    path('api/v2/careers', api.CareerDetailListApi.as_view(), name='career_list_api'),
    path('api/v2/careers/<int:id>',
         api.CareerDetailDetail.as_view(), name='career_detail_api'),
]
