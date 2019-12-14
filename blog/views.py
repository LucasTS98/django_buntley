from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

posts = [
        {
            'author': 'Lucas',
            'title': 'ola mundo',
            'content': 'first post',
            'date': 'hoje',
        },
        {
            'author': 'Lucca',
            'title': 'ola mundo 2',
            'content': 'second post',
            'date': 'hoje',
        }
    ]

def home(request):
    context = {
        'posts':posts
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')



    