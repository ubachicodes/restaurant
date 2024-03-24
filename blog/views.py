from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def blog(request):
    # Fetch all blog posts
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})