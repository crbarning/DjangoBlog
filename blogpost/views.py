from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def home(request):
    blogposts = Blogpost.objects.all()
    context = {
        'home': blogposts,
        'page_title': 'Christinas blog!',
    }
    return render(request, 'home.html', context)

def create(request):
    context = {
        'page_title': 'Post to the blog!',
    }
    return render(request, 'create.html', context)
