from django.contrib import admin

# Register your models here.
from .models import Category, Sun_Category, Product

admin.site.register(Category)
admin.site.register(Sun_Category)
admin.site.register(Product)