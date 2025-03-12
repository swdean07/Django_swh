from django.contrib import admin

from sports.models import Sports


# Register your models here.
@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    pass