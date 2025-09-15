from django.contrib import admin
from .models import ModelCategory, ModelAccount, ModelCoin, ModelTypeAccount


@admin.register(ModelCategory)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(ModelAccount)
class AdminAccount(admin.ModelAdmin):
    list_display = ('type', 'description')
    list_filter = ('type',)
    search_fields = ('type',)


@admin.register(ModelCoin)
class AdminCoin(admin.ModelAdmin):
    list_display = ('coin', 'country', 'symbol')
    list_filter = ('coin', 'country')
    search_fields = ('name',)


@admin.register(ModelTypeAccount)
class AdminTypeAccount(admin.ModelAdmin):
    list_display = ('type', 'description')
    list_filter = ('type',)
    search_fields = ('type',)
