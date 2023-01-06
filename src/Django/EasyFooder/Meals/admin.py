from django.contrib import admin

from .models import Meal


class MealAdmin(admin.ModelAdmin):
    model = Meal
    list_display = ('meal_id', 'name', 'price')


admin.site.register(Meal, MealAdmin)
