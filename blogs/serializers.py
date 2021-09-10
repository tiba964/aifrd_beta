from rest_framework import serializers
from .models import Blog, StoryBackgroundImage, StoryDetail, StoryAndBlog, Team, TeamBackgroundImage


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class StoryAndBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryAndBlog
        fields = '__all__'

class TeamBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamBackgroundImage
        fields = '__all__'


class StoryBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryBackgroundImage
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class StoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryDetail
        fields = '__all__'
        ordering = ['-story_date']
