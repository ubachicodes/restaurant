from django.shortcuts import render

# Create your views here.
from .models import Meals

def meal_list(request):
    meal_list = Meals.objects.all()

    context = {
        "meals": meal_list
    }

    return render(request, 'menu.html', {'menu_items': menu_items})



def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)

    context = {'meal_detail' : meal_detail}

    return render(request, 'meals/detail.html', context)