from django.shortcuts import render
from .models import Meal,Category

# Create your views here.
def menu(request):
    breakfast = Category.objects.get(name = 'breakfast')
    lunch = Category.objects.get(name = 'lunch')
    dinner = Category.objects.get(name = 'dinner')
    meals = Meal.objects.filter(category = breakfast)
    lunch_meals = Meal.objects.filter(category = lunch)
    dinner_meals = Meal.objects.filter(category = dinner)
    
    return render(request,'menu/menu.html',{'meals': meals, 'lunch_meals' : lunch_meals, 'dinner_meals' : dinner_meals})