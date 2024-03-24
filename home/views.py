from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # Fetch data for home page
    menu_items = Meals.objects.all()[:5]  # Fetching 5 menu items
    blog_posts = BlogPost.objects.all()[:3]   # Fetching 3 latest blog posts
    return render(request, 'home.html', {'meal_detail' : meal_detail, 'blog_posts': blog_posts})
