from django.contrib import admin
from .models import Blog, StoryAndBlog, StoryBackgroundImage, Team, StoryDetail, TeamBackgroundImage


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id',
    'bg_image_blog',
                    'blogs_image',
                    'blogs_title',
                    'blogs_date',
                    'blogs_desc',
                    'blogs_location',
                    ]

class StoryAndBlogAdmin(admin.ModelAdmin):
    list_display = ['id',
    'bg_image_story_bloag',
                    'image_bg_stories',
                    'text_bg_stories',
                    'image_bg_blogs',
                    'text_bg_blogs',
                    ]

class TeamBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'bg_image_temas',

                    ]

class StoryBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'bg_image_story',

                    ]

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'teams_image',
                    'teams_name',
                    'teams_desc',
                    ]


class StoryDetailAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'story_image_one',
                    'story_image_two',
                    'story_image_three',
                    'story_date',
                    'story_location',
                    'story_name',
                    'story_desc1',
                    'story_desc2',
                    'story_desc3',
                    'story_desc4',
                    'story_desc5',
                    'story_desc6',
                    'story_desc7',
                    ]



admin.site.register(StoryAndBlog, StoryAndBlogAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(StoryDetail, StoryDetailAdmin)
admin.site.register(Blog, BlogAdmin)

admin.site.register(TeamBackgroundImage, TeamBackgroundImageAdmin)
admin.site.register(StoryBackgroundImage, StoryBackgroundImageAdmin)