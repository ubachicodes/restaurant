from django.shortcuts import render

# Create your views here.
from .models import Meals

def meal_list(request):
    meal_list = Meals.objects.all()

    context = {
        "meals": meal_list
    }

    return render(request, 'meals/list.html', context)



def meal_detail(request, slug):
    pass
