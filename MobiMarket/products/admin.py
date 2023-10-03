from django.contrib import admin

from .models import Product, LikeProduct, MyProduct

admin.site.register(Product)
admin.site.register(MyProduct)
admin.site.register(LikeProduct)
