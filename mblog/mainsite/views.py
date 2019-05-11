from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append('No.{}: '.format(str(count)) + str(post) + '<br>')
        post_lists.append('<small>' + str(post.body) + '</small><br><br>')

    return HttpResponse(post_lists)

def homepage_render(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        print(post)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except Exception as e:
        print(e)
        return redirect('/')

