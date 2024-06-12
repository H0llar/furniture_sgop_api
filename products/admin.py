from django.contrib import admin

from products.models import Category, Brand, Furniture

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Furniture)
