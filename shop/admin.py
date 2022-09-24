from django.contrib import admin

# Register your models here.
from shop.models import Category, Item

admin.site.register(Category)
admin.site.register(Item)
