from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def home(request):
    return render(request, 'home.html')

def posts(request):
    blogposts = Blogpost.objects.all()
    count = blogposts.count()
    context = {
        'posts': blogposts,
        'count': count,
    }
    return render(request, 'posts.html', context)

def create(request):
    return render(request, 'create.html')
