from django.contrib import admin

from .models import Product, LikeProduct

admin.site.register(Product)
admin.site.register(LikeProduct)