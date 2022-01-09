from django.db import models
from .validators import validate_file_extension, validate_image_extension
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


REGION_TYPE = (
    ('Baghdad', "Baghdad"),
    ('Mousl', "Mousl"),
    ('Erbil', "Erbil"),
    ('Anbar', "Anbar"),
    ('Babylon', "Babylon"),
    ('Basra', "Basra"),
    ('Dhi Qar', "Dhi Qar"),
    ('Diyala', "Diyala"),
    ('Dohuk', "Dohuk"),
    ('Karbala', "Karbala"),
    ('KirKuk', "KirKuk"),
    ('Maysan', "Maysan"),
    ('Najaf', "Najaf"),
    ('Qaisiyah', "Qaisiyah"),
    ('Salahaddin', "Salahaddin"),
    ('Sulaymaniyah', "Sulaymaniyah"),
    ('Wasit', "Wasit"),
)

GENDER_TYPE = (
    ('Female', "Female"),
    ('Male', "Male"),
)



class Application(models.Model):

    full_name = models.CharField(max_length=200)

    email = models.EmailField(max_length=255, unique=True, db_index=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$',
        message="Phone number must be entered in the format: '+999999999'.\
             Up to 14 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17, unique=True)

    region = models.CharField(choices=REGION_TYPE, max_length=12)

    address = models.CharField(max_length=250, blank=True, null=True)

    gender = models.CharField(choices=GENDER_TYPE, max_length=6)

    english = models.CharField(
        default="English", max_length=7, blank=True, null=True)

    kurdish = models.CharField(
        default="Kurdish", max_length=7, blank=True, null=True)

    arabic = models.CharField(
        default="Arabic", max_length=6, blank=True, null=True)

    cover_letter = models.TextField()

    upload_cv = models.FileField(
        validators=[validate_file_extension],
        upload_to='uploadcv/', blank=False, null=False)

    def __str__(self):
        return (self.phone)

    def __str__(self):
        return (self.full_name)

    def __str__(self):
        return (self.email)


class VisionMissionValue(models.Model):
    image_bg = models.FileField(
        validators=[validate_image_extension], upload_to='background/vission_mission/', )
    Vission_Mission_Value_desc1 = models.CharField(
        max_length=300, default='', blank=True, )
    Vission_Mission_Value_desc1_ar = models.CharField(
        max_length=300, default='', blank=True, )
    Vission_Mission_Value_desc2 = models.CharField(
        max_length=300, default='', blank=True, )
    Vission_Mission_Value_desc2_ar = models.CharField(
        max_length=300, default='', blank=True, )
    vission_text = models.CharField(
        max_length=300, default='', blank=True, )
    vission_text_ar = models.CharField(
        max_length=300, default='', blank=True, )

    mission_text = models.CharField(
        max_length=300, default='', blank=True, )
    mission_text_ar = models.CharField(
        max_length=300, default='', blank=True, )
   


class Donate(models.Model):
    image_bg_donate = models.FileField(
        validators=[validate_image_extension], upload_to='background/donate/', )
    facebook_link = models.CharField(
        max_length=300, default='', blank=True, )
    twitter_link = models.CharField(
        max_length=300, default='',  blank=True,)
    instagram_link = models.CharField(
        max_length=300, default='',  blank=True,)
    location_donate = models.CharField(
        max_length=300, default='', blank=True, )
    location_donate_ar = models.CharField(
        max_length=300, default='', blank=True, )
    email_donate = models.CharField(
        max_length=300, default='', blank=True, )
    phone_donate = models.CharField(
        max_length=300, default='', blank=True, )


class Volunteer(models.Model):
    image_bg_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/volunteer/', )
class Replay(models.Model):
    image_bg_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/volunteer/', )

class WhatWeAreDoingBackgroundImage(models.Model):
    bg_image_what_we_are_doing = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoing/',default='', blank=True)
  

class About(models.Model):
    image_middle_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', )
    text_about = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about1 = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about1_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about2 = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about2_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about3 = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about3_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about4 = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about4_ar = models.TextField(
        max_length=1000, default='',  blank=True,)


class GetInvolved(models.Model):
    image_bg_getInvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', blank=True, )
    image_careers_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', blank=True, )
    text_careers_getinvolved = models.TextField(
        max_length=1000, default='', blank=True, )
    text_careers_getinvolved_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    image_joinus_getinvolved = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', blank=True, )
    text_joinus_getinvolved = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_joinus_getinvolved_ar = models.TextField(
        max_length=1000, default='',  blank=True,)


class WhoWeAre(models.Model):
    image_bg_whoweare = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', blank=True, )
    WhoWeAre_image1 = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/blogs/',  blank=True,)
    WhoWeAre_image2 = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/blogs/', blank=True, )
    WhoWeAre_image3 = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/blogs/', blank=True, )
   
    WhoWeAre_desc1 = models.TextField(
        max_length=1000, default='', blank=True, )
    WhoWeAre_desc1_ar = models.TextField(
        max_length=1000, default='', blank=True, )

    WhoWeAre_desc2 = models.TextField(
        max_length=1000, default='',  blank=True,)
    WhoWeAre_desc2_ar = models.TextField(
        max_length=1000, default='',  blank=True,)

    WhoWeAre_desc3 = models.TextField(
        max_length=1000, default='',  blank=True,)
    WhoWeAre_desc3_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    WhoWeAre_desc4 = models.TextField(
        max_length=1000, default='',  blank=True,)
    WhoWeAre_desc4_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
   

   
class Slider(models.Model):
    slide_image_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    slide_title_index = models.CharField(
        max_length=300, default='', blank=True, )
    slide_title_index_ar = models.CharField(
        max_length=300, default='', blank=True, )
    slide_subtitle_index = models.CharField(
        max_length=300, default='', blank=True, )
    slide_subtitle_index_ar = models.CharField(
        max_length=300, default='', blank=True, )


class Index(models.Model):
    image_about_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    text_about_index = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about_index_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    image_story_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    text_story_index = models.TextField(
        max_length=1000, default='', blank=True, )
    text_story_index_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    whatDoDetail_text = models.TextField(
        max_length=1000, default='', blank=True, )
    whatDoDetail_text_ar = models.TextField(
        max_length=1000, default='', blank=True, )


class WhatWeAreDoingDetail(models.Model):
    whatDoDetail_image_gallery = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoingDetails/', blank=True, )
   
    whatDoDetail_icon_name = models.CharField(
        max_length=300, default='', blank=True, )

    whatDoDetail_name = models.CharField(
        max_length=300, default='', blank=True, )
    whatDoDetail_name_ar = models.CharField(
        max_length=300, default='', blank=True, )

    whatDoDetail_desc1 = models.TextField(
        max_length=1000, default='', blank=True, )
    whatDoDetail_desc1_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    whatDoDetail_desc2 = models.TextField(
        max_length=1000, default='', blank=True, )
    whatDoDetail_desc2_ar = models.TextField(
        max_length=1000, default='', blank=True, )

    whatDoDetail_desc3 = models.TextField(
        max_length=1000, default='', blank=True, )
    whatDoDetail_desc3_ar = models.TextField(
        max_length=1000, default='', blank=True, )

    whatDoDetail_desc4 = models.TextField(
        max_length=1000, default='', blank=True, )

    whatDoDetail_desc4_ar = models.TextField(
        max_length=1000, default='', blank=True, )

