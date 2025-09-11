from django.contrib import admin
from models import ModelCategory


@admin.register(ModelCategory)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name')
