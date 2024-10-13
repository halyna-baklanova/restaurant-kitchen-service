from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from management.models import DishType, Dish, Cook

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "dish_type", "get_cooks"]
    list_filter = ["dish_type", ]
    search_fields = ["name"]

    def get_cooks(self, obj):
        return ", ".join([cook.last_name for cook in obj.cooks.all()])


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("social",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("social",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("social",)}),)
    actions = ["delete_selected_cooks"]

admin.site.register(DishType)
