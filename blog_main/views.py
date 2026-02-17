
# from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog
from assignment.models import About

def home(request):
   
    featured_post = Blog.objects.filter(is_featured = True, status="Published")
    recent_articles = Blog.objects.filter(is_featured=False, status="Published")
    try:
        about_us = About.objects.get()
    except:
        about_us = None
    print(recent_articles)
    context = {
     
        'featured_post' : featured_post,
        'recent_articles' : recent_articles,
        'about_us' : about_us
    }
    return render(request, 'home.html', context) 