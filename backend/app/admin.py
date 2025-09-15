from django.contrib import admin
from .models import ModelOperations, ModelImagens


class AdminImagens(admin.TabularInline):
    model = ModelImagens
    extra = 1


@admin.register(ModelOperations)
class AdminOperations(admin.ModelAdmin):
    list_display = ('name', 'accont_origin', 'accont_destination', 'date', 'value', 'coin')
    inlines = (AdminImagens,)