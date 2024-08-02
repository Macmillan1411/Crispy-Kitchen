from django.contrib import admin
from .models import Category, Meal



class MealModelAdmin(admin.ModelAdmin):
    list_filter = [
         "category",
        
    ]
    search_fields = (
        "name",
        
    )












# Register your models here.
admin.site.register(Category)
admin.site.register(Meal,MealModelAdmin)

