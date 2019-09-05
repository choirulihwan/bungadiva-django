from django.contrib import admin

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_per_page = 30

admin.site.register(Category, CategoryAdmin)