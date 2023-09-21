from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.TextField(verbose_name='Описание', max_length=500)
    photo = models.ImageField(
        verbose_name='Фото товара',
        upload_to='media/product_image',
        default='product_image/download.jpeg')
    available = models.BooleanField(verbose_name='В наличии', default=False)
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2)


class LikeProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    like = models.BooleanField(verbose_name='Понравившийся товар', default=False)
