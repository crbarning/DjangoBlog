from django.shortcuts import render, redirect
from .models import Blogpost
import json

# Create your views here.
def home(request):
    blogposts = Blogpost.objects.all()
    context = {
        'home': blogposts,
    }
    return render(request, 'home/home.html', context)

def all_posts(request):
    error_message = ''
    if request.method == 'POST':
        id = int(request.POST.get('post_id'))
        try:
            Blogpost.objects.get(id=id).delete()
        except:
            print('Error deleting post')
            error_message = 'Error deleting post'

    blogposts = Blogpost.objects.all().order_by('-id')
    context = {
        'home': blogposts,
        'error_message': error_message,
    }
    return render(request, 'home/all_posts_detailed.html', context)

def add_post(request):
    if request.method == 'GET':
        context = {
            'page_title':'Add a New Post!'
        }
        return render(request, 'home/add_post.html', context)

    else:
        new_post = Blogpost.objects.create(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            text = request.POST.get('text'),
        )
        new_post.save()
        return redirect(all_posts)


def single_post(request, post_id):
    selected_post = Blogpost.objects.get(id=post_id)
    context = {
        'page_title': getattr(selected_post, 'title'),
        'post': selected_post
    }
    return render(request, 'home/single_post.html', context)
