from django.contrib import admin

from coffee.models import Coffee


# Register your models here.
@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass