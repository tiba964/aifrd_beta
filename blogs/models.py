from django.db import models
from .validators import validate_image_extension
from django.utils.translation import gettext_lazy as _

from datetime import date


class Blog(models.Model):
    bg_image_blog = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/',default='', blank=True)
    blogs_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/',default='', blank=True)
    blogs_title = models.CharField(  max_length=300, default='', blank=True)
    blogs_title_ar = models.CharField(  max_length=300, default='', blank=True)

    blogs_date = models.DateField(default=date.today, blank=True)
    blogs_desc = models.TextField(
        max_length=1000, default='', blank=True)
    blogs_location = models.CharField(
        max_length=300, default='', blank=True)
    blogs_desc_ar = models.TextField(
        max_length=1000, default='', blank=True)
    blogs_location_ar = models.CharField(
        max_length=300, default='', blank=True)


class Team(models.Model):
   
    teams_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', blank=True)
    teams_name = models.CharField(
        max_length=300, default='', blank=True)

    teams_desc = models.TextField(
        max_length=1000, default='', blank=True)
    teams_name_ar = models.CharField(
        max_length=300, default='', blank=True)

    teams_desc_ar = models.TextField(
        max_length=1000, default='', blank=True)
        
class TeamBackgroundImage(models.Model):
    bg_image_temas = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/',default='', blank=True)
class StoryBackgroundImage(models.Model):
    bg_image_story = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/',default='', blank=True)
  

class StoryDetail(models.Model):

    story_image_one = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    story_image_two = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    story_image_three = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    story_date = models.DateField(default=date.today, blank=True)
    story_location = models.CharField(
        max_length=300, default='', blank=True)
    story_name = models.CharField(
        max_length=300, default='', blank=True)
    story_desc1 = models.CharField(
        max_length=120, default='', blank=True)
    story_desc2 = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc3 = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc4 = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc5 = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc6 = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc7 = models.TextField(
        max_length=1000, default='', blank=True)
    story_location_ar = models.CharField(
        max_length=300, default='', blank=True)
    story_name_ar = models.CharField(
        max_length=300, default='', blank=True)
    story_desc1_ar = models.CharField(
        max_length=120, default='', blank=True)
    story_desc2_ar = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc3_ar = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc4_ar = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc5_ar = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc6_ar = models.TextField(
        max_length=1000, default='', blank=True)
    story_desc7_ar = models.TextField(
        max_length=1000, default='', blank=True)

    class Meta:
        ordering = ['-story_date']


class StoryAndBlog(models.Model):
    bg_image_story_bloag = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_and_blogs/', blank=True)
    image_bg_stories = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_and_blogs/', blank=True)
    text_bg_stories = models.TextField(
        max_length=1000, default='', blank=True)
    text_bg_stories_ar = models.TextField(
        max_length=1000, default='', blank=True)
    image_bg_blogs = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_and_blogs/', blank=True)
    text_bg_blogs = models.TextField(
        max_length=1000, default='', blank=True)
    text_bg_blogs_ar = models.TextField(
        max_length=1000, default='', blank=True)
