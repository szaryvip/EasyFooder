from django.contrib import admin

from .models import Meal, Tag, Meal_tag, Order


class MealAdmin(admin.ModelAdmin):
    model = Meal
    list_display = ('name', 'price', 'get_tags')

    def get_tags(self, obj: Meal):
        meal_tags = Meal_tag.objects.filter(meal=obj)
        tags_print = "".join([f"{meal_tag.tag.name}, " for meal_tag in meal_tags])
        return tags_print[:-2] if tags_print else tags_print
    get_tags.short_description = "Tags"


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('name', 'get_meal_count')

    def get_meal_count(self, obj: Tag):
        return Meal_tag.objects.filter(tag=obj).count()
    get_meal_count.short_description = "Meal count"


class Meal_TagAdmin(admin.ModelAdmin):
    model = Meal_tag
    list_display = ('get_meal_name', 'get_tag_name')

    def get_meal_name(self, obj: Meal_tag):
        return obj.meal.name
    get_meal_name.short_description = "Meal name"

    def get_tag_name(self, obj: Meal_tag):
        return obj.tag.name
    get_tag_name.short_description = "Tag name"


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('date', 'get_username', 'get_meal_name', 'status')

    def get_username(self, obj: Order):
        return obj.user_id.username

    def get_meal_name(self, obj: Order):
        return obj.meal_id.name


admin.site.register(Meal, MealAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Meal_tag, Meal_TagAdmin)
admin.site.register(Order, OrderAdmin)
