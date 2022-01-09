from django.db import models
from .validators import validate_image_extension
from datetime import date
from django.utils.translation import gettext_lazy as _

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

JOB_TYPE_AR = (
    ('1', "دوام كامل"),
    ('2', "دوام جزئي"),
    ('3', "تدريب"),
)
class CareerDetail(models.Model):
   
    title = models.CharField(max_length=300, default='', null=True, blank=True)
    title_ar = models.CharField(max_length=300, default='', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description_ar = models.TextField(null=True, blank=True)

    working_hours = models.CharField(
        max_length=300, default='', null=True, blank=True)
    contract_duration = models.CharField(
        max_length=300, default='', null=True, blank=True)
    governorate = models.CharField(
        max_length=300, default='', null=True, blank=True)
    governorate_ar = models.CharField(
        max_length=300, default='', null=True, blank=True)
    job_type = models.CharField(
        choices=JOB_TYPE, max_length=1, null=True, blank=True)
    job_type_ar = models.CharField(
        choices=JOB_TYPE_AR, max_length=1, null=True, blank=True)
    
    location = models.CharField(
        max_length=300, default='', null=True, blank=True)
    location_ar = models.CharField(
        max_length=300, default='', null=True, blank=True)
    posted = models.DateField(default=date.today, null=True, blank=True)
    minimum_education = models.CharField(
        max_length=300, default='', null=True, blank=True)
    minimum_education_ar = models.CharField(
        max_length=300, default='', null=True, blank=True)
    minimum_experience = models.CharField(
        max_length=300, default='', null=True, blank=True)
    required_travel = models.CharField(
        max_length=150, default='', null=True, blank=True)
    required_travel_ar = models.CharField(
        max_length=150, default='', null=True, blank=True)
    no_of_jobs = models.PositiveIntegerField(default=1, null=True, blank=True)
    deadline = models.DateField(default=date.today, null=True, blank=True)
    puplished = models.DateField(default=date.today, null=True, blank=True)
       # Roles and Resposibilities
    role_1 = models.TextField(null=True, blank=True)
    role_1_ar = models.TextField(null=True, blank=True)
    role_2 = models.TextField(null=True, blank=True)
    role_2_ar = models.TextField(null=True, blank=True)
    role_3 = models.TextField(null=True, blank=True)
    role_3_ar = models.TextField(null=True, blank=True)
    role_4 = models.TextField(null=True, blank=True)
    role_4_ar = models.TextField(null=True, blank=True)
    role_5 = models.TextField(null=True, blank=True)
    role_5_ar = models.TextField(null=True, blank=True)
    role_6 = models.TextField(null=True, blank=True)
    role_6_ar = models.TextField(null=True, blank=True)
    role_7 = models.TextField(null=True, blank=True)
    role_7_ar = models.TextField(null=True, blank=True)
    role_8 = models.TextField(null=True, blank=True)
    role_8_ar = models.TextField(null=True, blank=True)
    role_9 = models.TextField(null=True, blank=True)
    role_9_ar = models.TextField(null=True, blank=True)
    role_10 = models.TextField(null=True, blank=True)
    role_10_ar = models.TextField(null=True, blank=True)

   

    # Qualifications & Preferred Skills
    skill_1 = models.TextField(null=True, blank=True)
    skill_1_ar = models.TextField(null=True, blank=True)
    skill_2 = models.TextField(null=True, blank=True)
    skill_2_ar = models.TextField(null=True, blank=True)
    skill_3 = models.TextField(null=True, blank=True)
    skill_3_ar = models.TextField(null=True, blank=True)
    skill_4 = models.TextField(null=True, blank=True)
    skill_4_ar = models.TextField(null=True, blank=True)
    skill_5 = models.TextField(null=True, blank=True)
    skill_5_ar = models.TextField(null=True, blank=True)
    skill_6 = models.TextField(null=True, blank=True)
    skill_6_ar = models.TextField(null=True, blank=True)
    skill_7 = models.TextField(null=True, blank=True)
    skill_7_ar = models.TextField(null=True, blank=True)
    skill_8 = models.TextField(null=True, blank=True)
    skill_8_ar = models.TextField(null=True, blank=True)
    skill_9 = models.TextField(null=True, blank=True)
    skill_9_ar = models.TextField(null=True, blank=True)
    skill_10 = models.TextField(null=True, blank=True)
    skill_10_ar = models.TextField(null=True, blank=True)

    

    def __str__(self):
        return self.title


class CareerList(models.Model):
    image_bg_career_list = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_list/', null=True, blank=True)


class CareerDetatilImage(models.Model):

    image_header_logo_sticky_career_detail_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_detail_image/', null=True, blank=True)
    image_footer_logo_career_detail_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_detail_image/', null=True, blank=True)
