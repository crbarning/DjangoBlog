from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def home(request):
    blogposts = Blogpost.objects.all()
    context = {
        'home': blogposts,
    }
    return render(request, 'home/home.html', context)


def single_post(request, post_id):
    selected_post = Blogpost.objects.get(id=post_id)
    context = {
        'page_title': getattr(selected_post, 'title'),
        'post': selected_post
    }
    return render(request, 'home/single_post.html', context)
