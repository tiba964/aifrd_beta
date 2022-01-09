from jobs.serializers import SliderSerializer
from django.contrib import admin
from .models import  Slider, VisionMissionValue, Application, WhatWeAreDoingBackgroundImage, WhoWeAre, Volunteer, Index, Donate, WhatWeAreDoingDetail, About, GetInvolved


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'region', 'address',
                    'gender', 'english', 'arabic', 'kurdish', 'cover_letter', 'upload_cv']


class DonateAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_donate',
                    'facebook_link',
                    'twitter_link',
                    'instagram_link',
                    'location_donate',
                     'location_donate_ar',
                    'email_donate',
                    'phone_donate',

                    ]


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'full_name',
                    'email',
                    'phone',
                    'subject',
                    'message',
                    ]


class GetInvolvedAdmin(admin.ModelAdmin):
    list_display = ['id',
    'image_bg_getInvolved',
                    'image_careers_getinvolved',
                    'image_joinus_getinvolved',
                    'text_careers_getinvolved',
                    'text_careers_getinvolved_ar',
                    'text_joinus_getinvolved',
                    'text_joinus_getinvolved_ar',
                    ]


class WhoWeAreAdmin(admin.ModelAdmin):
    list_display = ['id',
    'image_bg_whoweare',
                    'WhoWeAre_image1',
                    'WhoWeAre_image2',
                    'WhoWeAre_image3',
                    'WhoWeAre_desc1',
                    'WhoWeAre_desc2',
                    'WhoWeAre_desc3',
                    'WhoWeAre_desc4',
                     'WhoWeAre_desc1_ar',
                    'WhoWeAre_desc2_ar',
                    'WhoWeAre_desc3_ar',
                    'WhoWeAre_desc4_ar',
                   
                    ]


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_volunteer',

                    ]


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about',
                    'text_about1',
                    'text_about2',
                    'text_about3',
                 'text_about4',
                 'text_about_ar',
                    'text_about1_ar',
                    'text_about2_ar',
                    'text_about3_ar',
                 'text_about4_ar',
                    'image_middle_about',

                    ]

class WhatWeAreDoingBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'bg_image_what_we_are_doing',
                    ]


class VisionMissionValueAdmin(admin.ModelAdmin):
    list_display = ['id',
                   'image_bg',
                    'Vission_Mission_Value_desc1',
                    'Vission_Mission_Value_desc2',
                    'vission_text',
                    'mission_text',
'Vission_Mission_Value_desc1_ar',
                    'Vission_Mission_Value_desc2_ar',
                    'vission_text_ar',
                    'mission_text_ar',
                    ]


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'slide_image_index',
                    'slide_title_index',
                    'slide_subtitle_index',
                     'slide_title_index_ar',
                    'slide_subtitle_index_ar',

                    ]


class IndexAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about_index',
                     'text_about_index_ar',
                    'image_about_index',
                    'image_story_index',
                    'text_story_index',
                    'whatDoDetail_text',
                    'text_story_index_ar',
                    'whatDoDetail_text_ar',



                    ]


class WhatWeAreDoingDetailAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'whatDoDetail_image_gallery',
               
                    'whatDoDetail_name',
                    'whatDoDetail_desc1',
                    'whatDoDetail_desc2',
                    'whatDoDetail_desc3',
                    'whatDoDetail_desc4',
                    
                    'whatDoDetail_name_ar',
                    'whatDoDetail_desc1_ar',
                    'whatDoDetail_desc2_ar',
                    'whatDoDetail_desc3_ar',
                    'whatDoDetail_desc4_ar',
                    
                    'whatDoDetail_icon_name',
                    ]


admin.site.register(Index, IndexAdmin)
admin.site.register(Slider, SliderAdmin)

admin.site.register(WhatWeAreDoingBackgroundImage, WhatWeAreDoingBackgroundImageAdmin)
admin.site.register(GetInvolved, GetInvolvedAdmin)
admin.site.register(Donate, DonateAdmin)
# admin.site.register(Contact, ContactAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhoWeAre, WhoWeAreAdmin)
admin.site.register(VisionMissionValue, VisionMissionValueAdmin)
admin.site.register(WhatWeAreDoingDetail, WhatWeAreDoingDetailAdmin)
