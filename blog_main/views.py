
# from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
   
    featured_post = Blog.objects.filter(is_featured = True, status="Published")
    recent_articles = Blog.objects.filter(is_featured=False, status="Published")
    print(recent_articles)
    context = {
     
        'featured_post' : featured_post,
        'recent_articles' : recent_articles,
    }
    return render(request, 'home.html', context) 