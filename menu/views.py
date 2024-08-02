from django.shortcuts import render
from .models import Meal,Category

# Create your views here.
def menu(request):
    breakfast = Category.objects.get(name = 'breakfast')
    meals = Meal.objects.filter(category = breakfast)
    for meal in meals:
        print(meal)
    
    return render(request,'menu/menu.html',{'meals': meals})