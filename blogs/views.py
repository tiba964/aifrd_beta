from django.shortcuts import render
from .models import Blog, StoryAndBlog, StoryBackgroundImage, Team, StoryDetail, TeamBackgroundImage
from .serializers import BlogSerializer, StoryDetailSerializer, StoryAndBlogSerializer, TeamSerializer, TeamBackgroundImageSerializer
from django.http import HttpRequest
from .filters import StoryDetailFilter
from .form import StoryDetailForm
from django.core.paginator import Paginator


def blogs(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer(queryset, many=True)

    return render(request, 'blogs.html',
                  {
                      'data': serializer_class.data,
                  }
                  )

# def backgroundImage(request):
#     assert isinstance(request, HttpRequest)
#     queryset = BackgroundImage.objects.all()
#     serializer_class = BackgroundImageSerializer(queryset, many=True)

  
  
    
#     background_Image = BackgroundImage.objects.all()[:4]
#     context = {
#         'data': serializer_class.data,
#         'slider_show': background_Image,
      
#     }
#     return render(request, 'index.html', context)

def stories_list(request):

    stories = StoryDetail.objects.all().order_by('-story_date')
    storyBackgroundImage = StoryBackgroundImage.objects.all()
    # filters
    myfilter = StoryDetailFilter(request.GET, queryset=stories)
    stories = myfilter.qs

    # Show many contacts per page.
    paginator = Paginator(stories, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if stories:
        context = {'stories': page_obj, 'myfilter': myfilter,
        'storyBackgroundImage':storyBackgroundImage}  # template name

    else:
        context = {'message': "There are no stories available at the moment."}
    return render(request, 'stories.html', context)


def stories_detail(request, id):
    """Renders the create volunteer page."""
    stories = StoryDetail.objects.get(id=id)

    context = {'story': stories}
    return render(request, 'stories_detail.html', context)


def stories_and_blogs(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = StoryAndBlog.objects.all()
    serializer_class = StoryAndBlogSerializer(queryset, many=True)

    return render(request, 'StoriesAndBlogs.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def teams(request):
    """Renders the create teams page."""
    assert isinstance(request, HttpRequest)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer(queryset, many=True)
    bg_image_teams = TeamBackgroundImage.objects.all()
    context = {
'data': serializer_class.data, 
 'bg_image_teams': bg_image_teams,
        
    }
    
    return render(request, 'teams.html',context)