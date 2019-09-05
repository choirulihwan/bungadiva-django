from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Product


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('id', 'name', 'category', 'price')
    list_per_page = 30
    list_display_links = ('id', 'name')

admin.site.register(Product, ProductAdmin)
