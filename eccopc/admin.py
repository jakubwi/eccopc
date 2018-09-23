from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product, Category, SerialNumber
from . import models

class ProductInline(admin.TabularInline):
    model = models.Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug' )
    inlines = [ProductInline]
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'picture', 'body', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CustomUserAdmin(UserAdmin):
    list_display = ['username']
    model = CustomUser

class SerialNumberAdmin(admin.ModelAdmin):
    model = models.SerialNumber

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.SerialNumber, SerialNumberAdmin)